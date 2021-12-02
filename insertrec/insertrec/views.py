from django.shortcuts import render
from insertrec.models import insertdata
from insertrec.models import dispdata
import pyodbc


def connsql(request):
    conn=pyodbc.connect('Driver={Sql Server};'
                        'Server=DESKTOP-PEJFIPR\SQLEXPRESS;'
                        'Database=project;'
                        'trusted_Connection=yes;'
                        )
    cursor=conn.cursor()
    cursor.execute("select * from zipcodes")
    result=cursor.fetchall()
    
    return render(request,'index.html',{"dispdata":result})

def saverecords(request):
    conn=pyodbc.connect('Driver={Sql Server};'
                        'Server=DESKTOP-PEJFIPR\SQLEXPRESS;'
                        'Database=project;'
                        'trusted_Connection=yes;')
    if request.method=="POST": 
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('stmob'):
            insertstvalues=insertdata()
            insertstvalues.stname=request.POST.get('stname')
            insertstvalues.stemail=request.POST.get('stemail')
            insertstvalues.stmob=request.POST.get('stmob')
            cursor=conn.cursor()
            cursor.execute("insert into sttable values ('"+insertstvalues.stname+"','"+insertstvalues.stemail+"','"+insertstvalues.stmob+"')")
            cursor.commit()
            order = cursor.fetchval("stname")
            return render(request,'index.html', {"order": order})