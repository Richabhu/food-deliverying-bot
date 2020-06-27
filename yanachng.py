from flask import Flask,render_template,request
from flask_ask import Ask, statement, question, session, delegate,context
from flask_ask import request as req
import json
import time
import unidecode
import urllib
import sqlite3 as sql
import random


app=Flask(__name__)
ask=Ask(app,"/")

sess={}
cityglobe='cityglobe'
areaglobe='areaglobe'
itemstr='itemstr'
linkrec='linkrec'
hotelglobe='hotelglobe'
hotel_list='hotel_list'
citi='citi'
iitem_str_display='iitem_str_display'
item_cart='item_cart'
ll='ll'
hotel_str='hotel_str'
htl_str_dspl='htl_str_dspl'
price_list='price_list'
total='total'
order_str='order_str'
areaa='areaa'
bill_str='bill_str'
total_str='total_str'
lastcall='lastcall'
status=0;
#sess[userid][citi]=["bangalore","hyderabad","mumbai"]
#sess[userid][areaa]={"mubarakpet":"hyderabad","baba ali road":"hyderbad","cantonment":"mumbai","south bandra":"mumbai","channasandra":"bangalore","whitefield":"bangalore","jayanagar":"bangalore"}

@ask.launch
def start_skill():
	global sess
	welcome_message = 'Hi, I am yana.. I can order food for you. Mention your city and area '
	userid=context.System.user.userId
	print("launch")
	print(userid)
	sess[userid]={CHNGAREA:'',chngcity:'',lastcall:'launch',cityglobe:"",areaglobe:"",itemstr:"",linkrec:"",hotelglobe:"",hotel_list:[],citi:[],iitem_str_display:"",item_cart:[],ll:[],hotel_str:"",htl_str_dspl:"",price_list:{},total:0,order_str:'',areaa:{}}
	con=sql.connect("yana.db")
	cur = con.cursor()
	row=cur.execute("select city_name from city_table")
	sess[userid][item_cart]={}
	sess[userid][price_list]={}
	sess[userid][itemstr]=''
	sess[userid][iitem_str_display]=''
	for var in row:
		var=''.join(map(str,var))
		sess[userid][citi].append(var)
	row=cur.execute("select area_name,city_name from area_table a,city_table c where a.city_id = c.city_id")
	for var in row:
		var=list(var)
		sess[userid][areaa][var[0]]=var[1]
	return question(welcome_message)


@ask.intent("citycall_intent")
def city(city,area):
	global sess
	userid=context.System.user.userId
	sess[userid][lastcall]='city'
	con=sql.connect("yana.db")
	cur = con.cursor()
	#print(req.intent.slots.city.resolutions.resolutionsPerAuthority[0].values[0].value.name)
	if city is not None:
		x=req.intent.slots.city.resolutions.resolutionsPerAuthority[0].get('values','0')
		if x is not '0':
			if req.intent.slots.city.resolutions.resolutionsPerAuthority[0]['values']:
				city = req.intent.slots.city.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
		elif req.intent.slots.city.resolutions.resolutionsPerAuthority[1].get('values','0') is not '0':
				if req.intent.slots.city.resolutions.resolutionsPerAuthority[1]['values']:
					city = req.intent.slots.city.resolutions.resolutionsPerAuthority[1]['values'][0]['value']['name']

	if area is not None:
		x=req.intent.slots.area.resolutions.resolutionsPerAuthority[0].get('values','0')
		if x is not '0':
			if req.intent.slots.area.resolutions.resolutionsPerAuthority[0]['values']:
				area = req.intent.slots.area.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
		elif req.intent.slots.area.resolutions.resolutionsPerAuthority[1].get('values','0') is not '0':
				if req.intent.slots.area.resolutions.resolutionsPerAuthority[1]['values']:
					area = req.intent.slots.area.resolutions.resolutionsPerAuthority[1]['values'][0]['value']['name']
	#print(deviceglId)
	if area is None and city is not None:
		city=city.lower()
		print(sess)
		print(sess[userid][citi])
		
		if city in sess[userid][citi]:
			if sess[userid][cityglobe]=="":
				sess[userid][cityglobe]=city
				return question("pls enter the area you are looking for..!")
			else:
				if sess[userid][cityglobe]==city:
					return question("please enter the area you are looking for")
				elif sess[userid][cityglobe] is not city:
					sess[userid][chngcity]=city
					status=1
					return question("You entered different city earlier say yes if you want to change it your cart will get reset")
		else:
			city_join=" ".join(sess[userid][citi])
			city_send="sorry we do not serve in this city :\n these are cities we serve:"+city_join+"\n select your city from above list and write ypor area"
			return question(city_send)
	elif area is not None and city is None:
		area=area.lower()	
		citychosed=sess[userid][areaa][area]
		sess[userid][areaglobe]=area
		if sess[userid][cityglobe] is not "":
			if citychosed==sess[userid][cityglobe]:
				sess[userid][hotel_list]=[]
				sess[userid][item_cart]=[]
				row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(sess[userid][cityglobe],sess[userid][areaglobe]))
				for var in row:
					var=''.join(map(str,var))   
					sess[userid][hotel_list].append(var)

				sess[userid][hotel_str]="\r\n-> ".join(map(str,sess[userid][hotel_list]))
				sess[userid][hotel_str]="->"+sess[userid][hotel_str]
				sess[userid][htl_str_dspl]=" ".join(map(str,sess[userid][hotel_list]))
				print(sess[userid][hotel_str])
				sess[userid][hotel_list]=[]
				return question("enter restaurant name from where you wanna order? The hotels available are:  "+sess[userid][htl_str_dspl]).standard_card(title="hotels available",text=sess[userid][hotel_str],large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
			else:
				sess[userid][chngarea]=area
				status=2
				return question("You choosed different city earlier and this area belongs to different city would you like to make changes your cart will become empty doing so")	
		else:
			sess[userid][cityglobe]=citychosed
			sess[userid][areaglobe]=area
			row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(sess[userid][cityglobe],sess[userid][areaglobe]))
			for var in row:
				var=''.join(map(str,var))   
				sess[userid][hotel_list].append(var)

			sess[userid][hotel_str]="\r\n-> ".join(sess[userid][hotel_list])
			sess[userid][hotel_str]="->"+sess[userid][hotel_str]
			sess[userid][htl_str_dspl]=", ".join(sess[userid][hotel_list])
			print(sess[userid][hotel_str])
			sess[userid][hotel_list]=[]
			return question("enter restaurant name from where you wanna order?The hotels available are:  "+sess[userid][htl_str_dspl]).standard_card(title="hotels available",text=sess[userid][hotel_str],large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
	else:
		city=city.lower()
		area=area.lower()
		if city not in sess[userid][citi]:
			city=city.lower()
			area=area.lower()
			city_join=" ".join(sess[userid][citi])
			city_send="Either your city is not available :\n these are cities we serve:"+city_join+"\n select your city from above list and write ypor area"
			return question(city_send)
		elif area not in sess[userid][areaa]:
			areaserved=[]
			if sess[userid][areaa][area] == city:
				areaserved.append(area)
			area_served_string=" ".join(areaserved)

			#areaserved=list(sess[userid][areaa].keys())
			
			return question("WE serve in dese areas:\n"+area_served_string+"\n chhose your area")
		else:
			sess[userid][cityglobe]=city
			sess[userid][areaglobe]=area
			row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(sess[userid][cityglobe],sess[userid][areaglobe]))
			for var in row:
				var=''.join(map(str,var))   
				sess[userid][hotel_list].append(var)
			sess[userid][htl_str_dspl]=" ".join(sess[userid][hotel_list])
			

			sess[userid][hotel_str]="\r\n-> ".join(sess[userid][hotel_list])
			sess[userid][hotel_str]="->"+sess[userid][hotel_str]

			print(sess[userid][hotel_str])
			sess[userid][hotel_list]=[]
			return question("enter restaurant name from where you wanna order?   The hotels available are:   "+sess[userid][htl_str_dspl]).standard_card(title="hotels available",text=sess[userid][hotel_str],large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
			#return question("Enter your restaurant from where you wana order")

@ask.intent("hotelcall_intent")
def hotel(hotels):
	userid=context.System.user.userId
	sess[userid][lastcall]='hotel'
	sess[userid][item_cart]={}
	if hotels is not None:
		x=req.intent.slots.hotels.resolutions.resolutionsPerAuthority[0].get('values','0')
		if x is not '0':
			if req.intent.slots.hotels.resolutions.resolutionsPerAuthority[0]['values']:
				hotels = req.intent.slots.hotels.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
		elif req.intent.slots.hotels.resolutions.resolutionsPerAuthority[1].get('values','0') is not '0':
				if req.intent.slots.hotels.resolutions.resolutionsPerAuthority[1]['values']:
					hotels = req.intent.slots.hotels.resolutions.resolutionsPerAuthority[1]['values'][0]['value']['name']
	
	con=sql.connect("yana.db")
	cur = con.cursor()
	if sess[userid][areaglobe] is "" and sess[userid][cityglobe] is "":
		return question("pls select ur city and area")

	row=cur.execute("select hotel_name from hotel_table h,city_table c,area_table a where h.city_id=c.city_id and a.area_id=h.area_id and c.city_name='%s' and  a.area_name='%s'"%(sess[userid][cityglobe],sess[userid][areaglobe]))
	for var in row:
		var=''.join(map(str,var))   
		sess[userid][hotel_list].append(var)
	hotel_set=set(sess[userid][hotel_list])
	sess[userid][hotel_list]=list(hotel_set)
	sess[userid][hotel_str]="".join(sess[userid][hotel_list])
	sess[userid][itemstr]=""
	sess[userid][iitem_str_display]=""
	sess[userid][linkrec]=""
	if hotels in sess[userid][hotel_list]:
		print(sess[userid][hotel_list])
		sess[userid][hotelglobe]=hotels
		itemlist=[]
		itemlist_display=[]
		rowfood=cur.execute("select i.item_name,price,h.hotel_link from hotel_table h,item_table i,menu_table m where h.hotel_id=m.hotel_id and i.item_id=m.item_id and h.hotel_name='%s'"%(sess[userid][hotelglobe]))
		sess[userid][ll] = rowfood.fetchall()
		for rowvar in sess[userid][ll]:
			rowvar=list(rowvar)
			#item_list.append(rowvar)
			itemlist_display.append(rowvar[0])
			sess[userid][price_list][rowvar[0]]=rowvar[1]
			lenn=25-len(rowvar[0])
			for i in range(lenn):
				rowvar[0]=rowvar[0]+'-'
			itemlist.append(rowvar[0]+""+str(rowvar[1])+"/-")
			#itemstr_display=
			sess[userid][itemstr]="\r\n.->".join(map(str,itemlist))
			sess[userid][itemstr]="->"+sess[userid][itemstr]
			sess[userid][hotel_str]="".join(map(str,itemlist))
			sess[userid][iitem_str_display]="...".join(map(str,itemlist_display))	
			sess[userid][linkrec]=rowvar[2]
		if len(sess[userid][ll]) >0:
			sess[userid][item_cart]={}
			return question("select the food which yu wanna order. We supply "+sess[userid][iitem_str_display]).standard_card(title="menu...........................................price",text=sess[userid][itemstr],large_image_url=sess[userid][linkrec])
		else:
			return question("we dont serve anything here")
	return question("Either the hotel is not available in this area or we dont serve this hotel..THe hotel served in this area  is:\r\n"+sess[userid][hotel_str])

@ask.intent('additem_intent')
def callingitem(number,item):
	userid=context.System.user.userId
	sess[userid][lastcall]='additem'
	food_list=[]
	dict_food={}
	if item is not None:
		x=req.intent.slots.item.resolutions.resolutionsPerAuthority[0].get('values','0')
		if x is not '0':
			if req.intent.slots.item.resolutions.resolutionsPerAuthority[0]['values']:
				item = req.intent.slots.item.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
		elif req.intent.slots.item.resolutions.resolutionsPerAuthority[1].get('values','0') is not '0':
				if req.intent.slots.item.resolutions.resolutionsPerAuthority[1]['values']:
					item = req.intent.slots.item.resolutions.resolutionsPerAuthority[1]['values'][0]['value']['name']
	#print("reb"+number)
	for row in sess[userid][ll]:
		f=row[0]
		p=row[1]
		food_list.append(f)
		dict_food[f]=p
		
	print(dict_food)
	if sess[userid][hotelglobe] is not "":
		if number is None and item is not None:
			if item in food_list:
				if item not in sess[userid][item_cart]:
					sess[userid][item_cart][item]=1
				else:
					sess[userid][item_cart][item]+=1
				print("cart")
				print(sess[userid][item_cart])
				return question("total "+str(sess[userid][item_cart][item])+" "+item+"?").standard_card(title="menu...........................................price",text=sess[userid][itemstr],large_image_url=sess[userid][linkrec])
			else:
				return question("pls select the food from given menu  We supply "+sess[userid][iitem_str_display]).standard_card(title="menu...........................................price",text=sess[userid][itemstr],large_image_url=sess[userid][linkrec])
		elif number is not None and item is not None:
			if item in food_list:
				if item not in sess[userid][item_cart]:
					sess[userid][item_cart][item]=int(number)
				else:
					sess[userid][item_cart][item]=int(number)
				print("CART")
				print(sess[userid][item_cart])
				return question("total "+str(sess[userid][item_cart][item])+" "+item+"?").standard_card(title="menu...........................................price",text=sess[userid][itemstr],large_image_url=sess[userid][linkrec])
			else:
				return question("Sorry we couldnt identify that..pls select the food from menu which yu wanna order. We supply "+sess[userid][iitem_str_display]).standard_card(title="menu...........................................price",text=sess[userid][itemstr],large_image_url=sess[userid][linkrec])
	else:
		if sess[userid][areaglobe] is not "":
			return question("pls select the hotel from the required list. The hotels available are:   "+sess[userid][htl_str_dspl]).standard_card(title="hotels available",text=sess[userid][hotel_str],large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
		else:
			return question("pls select the area and city")

#@ask.intent('AMAZON.CancelIntent')
def cancelorder():
	userid=context.System.user.userId
	con=sql.connect("yana.db")
	cur = con.cursor()
	#cur.execute('delete from accounts_table where user_id="%s"'%userid)
	start_skill()
	return question("Your previous order has been cancelled.. if you wanna place another other. pls enter your city and area")


@ask.intent('billing_intent')
def bill(yes,no):
	userid=context.System.user.userId
	sess[userid][lastcall]='biller'
	print("bill")
	print(userid)
	if yes is None and no is None:
		if not sess[userid][item_cart]:
			if sess[userid][areaglobe] is "":
				return question("you havent selected the area please enter your area from  where you wana order the food")
			elif sess[userid][hotelglobe] is "":
					lp=sess[userid][hotel_str].split("\r\n->")
					lp=list(''.join(lp))
					lp.remove('-')
					lp.remove('>')
					sess[userid][htl_str_dspl]=''.join(lp)
					return question("please select the hotel..... hotels in this area are: ..."+sess[userid][htl_str_dspl]).standard_card(title="hotels available",text=sess[userid][hotel_str],large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
			else:
					return question("please select some item from the list......"+sess[userid][iitem_str_display]).standard_card(title="menu...........................................price",text=sess[userid][itemstr],large_image_url=sess[userid][linkrec])
		else:
			calculate()
			return question('your order is: ...'+sess[userid][order_str]+'.. Do you want to confirm  the order? or you can continue to add the item').standard_card(title="Bill",text=sess[userid][bill_str],large_image_url="https://bafnasweather.000webhostapp.com/IMG_20180318_113652_Bokeh__01__01.jpg")
	else:
		if yes is not None and no is None:
			if sess[userid][item_cart] is None:
				return question('please select the item')
			elif sess[userid][total] is 0:
					calculate()
					ran=random.random()
					con=sql.connect("yana.db")
					cur = con.cursor()
					cur.execute('select user_id from user_table where user_id="%s"'%userid)
					temp=cur.fetchall()
					if len(temp)==0:
						cur.execute("INSERT INTO user_table (user_id)"
                    				"VALUES(?)",(userid,))
					con.commit()
					cur.execute("INSERT INTO accounts_table (order_id,user_id,all_item_name,total_bill,feedback_status)"
            					"VALUES(?,?,?,?,?)",(ran,userid,sess[userid][order_str],sess[userid][total],"null"))
					con.commit()
			if sess[userid][total] != 0:
				return question('order is placed and total bill is '+str(sess[userid][total])).simple_card(title="Final BIll",content=sess[userid][total_str])
			else:
				return question('cart is empty please select items from the hotel')
		elif yes is not None and no is not None:
				return question('please say either yes or no not the both we get confused right?')
		elif no is not None:
				return question('you can continue to add or can cancel the order')

def calculate():
	userid=context.System.user.userId
	sess[userid][bill_str]=""
	sess[userid][total_str]=""
	sess[userid][total]=0
	for key in sess[userid][item_cart]:
		sess[userid][order_str] +='...'+str(sess[userid][item_cart][key])+' '+key
		sess[userid][bill_str]+='\r\n->'+str(sess[userid][item_cart][key])+' '+key
		lenn=23-len(key)-5
		for i in range(lenn):
			sess[userid][bill_str]=sess[userid][bill_str]+'-'
		sess[userid][bill_str]+=str(sess[userid][price_list][key]*sess[userid][item_cart][key])+"/-"
		sess[userid][total]+=sess[userid][price_list][key]*sess[userid][item_cart][key]
		sess[userid][total_str]=sess[userid][bill_str]+"\r\n\n"+"Total___________"+str(sess[userid][total])+'/-'

@ask.intent('AMAZON.FallbackIntent')
def fallhere():
	global sess
	userid=context.System.user.userId
	if sess[userid][lastcall] is 'launch':
		f=open('fallback.txt',"a")
		return question("i din't get that you have to enter the city and area to proceed").simple_card(title="din't understand you sorry",content='if i was wrong i will improve my self with time now you have to add city and area for now')
	elif sess[userid][lastcall] is "city":
			if sess[userid][areaglobe] is "":
				return question("i din't get that you have to select the area so that i can list you the hotel in the area").simple_card(title="din't get you",content="i din't get you you have to select the area so that i can list you the area")
			else:
				return question("sorry i din't get that you have to enter the hotel name pls enter the hotel so that we can select the food to eat").simple_card(title="some issue occured in understanding you",content="you have to enter the hotel name pls enter the hotel so that we can select the food to eat")
	elif sess[userid][lastcall] is "hotel":
			if sess[userid][hotelglobe] is "":
				return question("sorry i din't get that you have to enter the hotel name pls enter the hotel so that we can select the food to eat").simple_card(title="some issue occured in understanding you",content="you have to enter the hotel name pls enter the hotel so that we can select the food to eat")
			else:
				return question("sorry i din't get that you can start adding itemn to cart or say done if you have already entered the items").standard_card(title="din't get you please select the item to enter",content="you have to enter the item or say done to place the order")
	elif sess[userid][lastcall] is "additem":
			return question("sorry i din't get that you can continue adding the item to the cart or say done to place the order in your cart if any")
	else:
		return question("sorry i din't get that! you can say yes to confirm and place the order if you have added your required items in the cart")

if __name__=="__main__":        
	app.run(debug="True",port=5005)
