from flask import Flask,render_template,request
from flask_ask import Ask, statement, question, session, delegate,context
from flask_ask import request as req
import json
import time
import requests
import unidecode
import urllib
import sqlite3 as sql


app=Flask(__name__)
ask=Ask(app,"/")



#citi=["bangalore","hyderabad","mumbai"]
cityglobe=""
areaglobe=""
itemstr=""
linkrec=""
hotelglobe=""
hotel_list=[]
citi=[]
iitem_str_display=""
areaa={}
item_cart={}
ll=[]
hotel_str=""
hotel_str_display=""
#areaa={"mubarakpet":"hyderabad","baba ali road":"hyderbad","cantonment":"mumbai","south bandra":"mumbai","channasandra":"bangalore","whitefield":"bangalore","jayanagar":"bangalore"}

@ask.launch
def start_skill():
    welcome_message = 'Hi, I am yana.. I can order food for you. Mention your city area '
    #uid=context.System.user.userId
    #did=context.System.device.deviceId
    #print(uid," ",did)
    con=sql.connect("yana.db")
    cur = con.cursor()
    row=cur.execute("select city_name from city_table")
    global citi
    for var in row:
    	var=''.join(map(str,var))   
    	citi.append(var)
    row=cur.execute("select area_name,city_name from area_table a,city_table c where a.city_id = c.city_id")
    global areaa
    for var in row:
    	var=list(var)
    	areaa[var[0]]=var[1]

    print(citi)
    print(areaa)
    return question(welcome_message)
    
@ask.intent("YesOrderIntent")
def yesorder():
	city_join=" ".join(city)
	city_send="these are cities we serve:"+city_join+"\n select your city from above list and write ypor area"
	return question(city_send) 



@ask.intent("citycall_intent")
def city(city,area):
	global cityglobe
	global areaglobe
	global citi
	global hotel_list
	global hotelglobe
	con=sql.connect("yana.db")
	cur = con.cursor()
	#print(req.intent.slots.city.resolutions.resolutionsPerAuthority[0].values[0].value.name)
	if city is not None and req.intent.slots.city.resolutions.resolutionsPerAuthority[0]['values']:
		city = req.intent.slots.city.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
	if area is not None and req.intent.slots.area.resolutions.resolutionsPerAuthority[0]['values']:
		area = req.intent.slots.area.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
	print(cityglobe)
	print(area)
	#print(deviceglId)
	if area is None and city is not None:
		city=city.lower()
		print(citi)
		
		if city in citi:
			cityglobe=city
			print(cityglobe)
			return question("pls enter the area you are looking for..!")
		else:
			city_join=" ".join(citi)
			city_send="sorry we do not serve in this city :\n these are cities we serve:"+city_join+"\n select your city from above list and write ypor area"
			return question(city_send)
	elif area is not None and city is None:
		area=area.lower()
		citychosed=areaa[area]
		areaglobe=area
		if cityglobe is not "":
			if citychosed==cityglobe:
				hotel_list=[]
				row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(cityglobe,areaglobe))
				for var in row:
					var=''.join(map(str,var))   
					hotel_list.append(var)

				hotel_str="\r\n-> ".join(map(str,hotel_list))
				hotel_str="->"+hotel_str
				hotel_str_display=" ".join(map(str,hotel_list))
				print(hotel_str)
				hotel_list=[]
				return question("enter restaurant name from where you wanna order? The hotels available are:  "+hotel_str_display).standard_card(title="hotels available",text=hotel_str,large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
			else:
				return question("You choosed different city earlier and this area belongs to different city")	
		else:
			cityglobe=citychosed
			areaglobe=area
			row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(cityglobe,areaglobe))
			for var in row:
				var=''.join(map(str,var))   
				hotel_list.append(var)

			hotel_str="\r\n-> ".join(hotel_list)
			hotel_str="->"+hotel_str
			hotel_str_display=" ".join(hotel_list)
			print(hotel_str)
			hotel_list=[]
			return question("enter restaurant name from where you wanna order?The hotels available are:  "+hotel_str_display).standard_card(title="hotels available",text=hotel_str,large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
	else:
		city=city.lower()
		area=area.lower()
		if city not in citi:
			city=city.lower()
			area=area.lower()
			city_join=" ".join(citi)
			city_send="Either your city is not available :\n these are cities we serve:"+city_join+"\n select your city from above list and write ypor area"
			return question(city_send)
		elif area not in areaa:
			areaserved=[]
			if areaa[area] == city:
				areaserved.append(area)
			area_served_string=" ".join(areaserved)

			#areaserved=list(areaa.keys())
			
			return question("WE serve in dese areas:\n"+area_served_string+"\n chhose your area")
		else:
			cityglobe=city
			areaglobe=area
			row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(cityglobe,areaglobe))
			for var in row:
				var=''.join(map(str,var))   
				hotel_list.append(var)
			hotel_str_display=" ".join(hotel_list)
			

			hotel_str="\r\n-> ".join(hotel_list)
			hotel_str="->"+hotel_str

			print(hotel_str)
			hotel_list=[]
			return question("enter restaurant name from where you wanna order?   The hotels available are:   "+hotel_str_display).standard_card(title="hotels available",text=hotel_str,large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
			#return question("Enter your restaurant from where you wana order")

@ask.intent("hotelcall_intent")
def hotel(hotels):
	global areaglobe
	global hotelglobe
	global cityglobe
	global hotel_list
	global itemstr
	global linkrec
	global item_cart
	global iitem_str_display
	global ll
	global hotel_str
	global hotel_str_display
	item_cart={}
	if hotels is not None and req.intent.slots.hotels.resolutions.resolutionsPerAuthority[0]['values']:
		hotels = req.intent.slots.hotels.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
	
	con=sql.connect("yana.db")
	cur = con.cursor()
	if areaglobe is "" and cityglobe is "":
		return question("pls select ur city and area")
	print("sej",cityglobe)
	print(areaglobe)

	row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(cityglobe,areaglobe))
	for var in row:
		var=''.join(map(str,var))   
		hotel_list.append(var)
	hotel_set=set(hotel_list)
	hotel_list=list(hotel_set)
	hotel_str="".join(hotel_list)
	itemstr=""
	iitem_str_display=""
	linkrec=""
	if hotels in hotel_list:
		print(hotel_list)
		hotelglobe=hotels
		itemlist=[]
		itemlist_display=[]
		rowfood=cur.execute("select i.item_name,price,h.hotel_link from hotel_table h,item_table i,menu_table m where h.hotel_id=m.hotel_id and i.item_id=m.item_id and h.hotel_name='%s'"%(hotelglobe))
		ll = rowfood.fetchall()
		for rowvar in ll:
			rowvar=list(rowvar)
			print(str(rowfood)+"jxfood")

			print(str(rowvar)+"rowvar")
			#item_list.append(rowvar)
			itemlist_display.append(rowvar[0])
			lenn=25-len(rowvar[0])
			for i in range(lenn):
				rowvar[0]=rowvar[0]+'-'
			itemlist.append(rowvar[0]+""+str(rowvar[1])+"/-")
			#itemstr_display=
			itemstr="\r\n.->".join(map(str,itemlist))
			itemstr="->"+itemstr
			hotel_str="".join(map(str,itemlist))
			iitem_str_display=" ".join(map(str,itemlist_display))	
			linkrec=rowvar[2]
		print(itemstr)
		print(hotel_str)
		print(ll)
		if len(ll) >0:
			item_cart={}
			return question("select the food which yu wanna order. We supply "+iitem_str_display).standard_card(title="menu...........................................price",text=itemstr,large_image_url=linkrec)
		else:
			return question("we dont serve anything here")
	return question("Either the hotel is not available in this area or we dont serve this hotel..THe hotel served in this area  is:\r\n"+hotel_str)

@ask.intent('additem_intent')
def callingitem(number,item):
	global item_cart
	global iitem_str_display
	global itemstr
	global hotel_str
	global hotel_str_display
	global linkrec
	print("cghh")
	food_list=[]
	price_list=[]
	dict_food={}

	#print("reb"+number)
	for row in ll:
		f=row[0]
		p=row[1]
		food_list.append(f)
		price_list.append(p)
		dict_food[f]=p
		
	print(dict_food)
	if hotelglobe is not "":
		if number is None and item is not None:
			if item in food_list:
				if item not in item_cart:
					item_cart[item]=1
				else:
					item_cart[item]+=1
				print("cart")
				print(item_cart)
				return question("to add more to cart, select the food which yu wanna order. We supply "+iitem_str_display).standard_card(title="menu...........................................price",text=itemstr,large_image_url=linkrec)
			else:
				return question("pls select the food from given menu  We supply "+iitem_str_display).standard_card(title="menu...........................................price",text=itemstr,large_image_url=linkrec)
		elif number is not None and item is not None:
			if item in food_list:
				if item not in item_cart:
					item_cart[item]=int(number)
				else:
					item_cart[item]+=int(number)
				print("CART")
				print(item_cart)
				return question("to add more to cart,select the food which yu wanna order. We supply "+iitem_str_display).standard_card(title="menu...........................................price",text=itemstr,large_image_url=linkrec)
			else:
				return question("Sorry we couldnt identify that..pls select the food from menu which yu wanna order. We supply "+iitem_str_display).standard_card(title="menu...........................................price",text=itemstr,large_image_url=linkrec)
	else:
		if areaglobe is not "":
			return question("pls select the hotel from the required list. The hotels available are:   "+hotel_str_display).standard_card(title="hotels available",text=hotel_str,large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
		else:
			return question("pls select the area and city")
		


		
	
	#return question(cityglobe).standard_card(title="tawa-roti",text="This is a awsome chapati i have prepared wth my awsome hand",large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
def noorder():
	msg="i am  not sure then why did you called me"	
	return statement(msg)
	


if(__name__=="__main__"):        
	app.run(debug="True",port=5005)

