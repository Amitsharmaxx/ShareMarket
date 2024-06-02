import mysql.connector #MySQL Connectors provide connectivity to the MySQL server for client programs.

import matplotlib.pyplot as plt #visualizations in Python

conn=mysql.connector.connect(
  host="localhost",
  user="root",
  password="rd11",
  database="share_market",
  
  )
print("Connected")



def createaccount():
      cur=conn.cursor()
      username=input("\tENTER YOUR USER NAME : ")
      password=input("\tENTER YOUR USER PASSWORD : ")
      mobile_no=input("\tENTER YOUR MOBILE NO. : ")
      gender = input("\tENTER YOUR GENDER :")
     
      cur=conn.cursor()
      query3="select * from user"
      cur.execute(query3)
      rs=cur.fetchall()
     
      query1="INSERT INTO user VALUES('{}','{}','{}','{}')".format(username,password,mobile_no,gender)
      cur.execute(query1)
      cur.execute("commit")



def login():
      cur=conn.cursor()
      username=input("\tEnter username:")
      passsword=input("\tEnter password:")
      query1="select passsword from user where username='{}'and passsword='{}'".format(username,passsword)

      cur.execute(query1)
      
      check=cur.fetchone()
      if check==None:
          print("Password Invalid,try again")
          for i in check:
              print(i)
              if i==passsword:
                  print("*"*70)
                  print("\t\tWELCOME BACK")
                  print("*"*70)
                  break
              else:
                  print("\tPassword invalid Try again")
                  continue



def investment():
      cur=conn.cursor()
      query3="select * from company_details;"
      cur.execute(query3)
      print("\t","*"*56)
      rs=cur.fetchall()
      print("\t","|","Sno","|"," Company  Name","      |","   AVG Investment Return""|",)
      print("\t","*"*56)
      for i in rs:
        print("\t","|  ",i[0],"|","\t",i[1],"\t\t",i[2],"\t\t|")
        print("\t","*"*56)
        
      company_name= input("\tEnter the company in which you want to invest?")
      investment=int(input("\tHow much money do you want to invest?"))
      years=int(input("\tFor how many years do you want to invest?"))
      query1="select avg_investment_return from company_details where company_name='{}'".format(company_name)
      cur.execute(query1)
      records=cur.fetchall()
     
      for row in records:
            avg_investment_return=(row[0])
           
      total=(((avg_investment_return*investment)/100)*12 ) + investment
      print("\tEstimated Earning :",total)



def graphical_growth():
  from matplotlib import pyplot as plt
  import numpy as np
  cur=conn.cursor()
  query1="select * from company_details"
  cur.execute(query1)
  a=cur.fetchall()
  co=[]
  av=[]
  for i in a:
    co.append(i[1])
    av.append(i[2])
  plt.pie(av,labels=co)
  plt.show()



def update():
    cur=conn.cursor()
    print("*"*70)
    company_name=input("\tEnter company name")
    avg_investment_return=float(input("\tEnter the avg_investment_return"))
    print("*"*70)
    print("\t\tRECORD UPDATED")

    query2=("update company_details set avg_investment_return={} where company_name='{}'".format(avg_investment_return,company_name))
    cur.execute(query2)
    cur.execute("commit")



def delete():
    cur=conn.cursor()
    print("*"*70)
    company_name=input("\t\tEnter company name")
    print("*"*70)
    print("\t\tRECORD DELETED")

    query2=("delete from company_details  where company_name='{}'".format(company_name))
    cur.execute(query2)
    cur.execute("commit")



def insert():
    cur=conn.cursor()
    print("*"*70)
    query1=("select count(*) from company_details")
    cur.execute(query1)
    company_name = input("\t\tEnter company name:")
    avg_investment_return=float(input("\t\tEnter the avg_investment_return:"))
    print("*"*70)
    print("\t\tRECORD INSERTED")

    rows = cur.fetchone()
    for i in rows:
        sn=i

        break
    sno = sn+1

    query2 = ("insert into  company_details values('{}','{}',{})".format(sno,company_name,avg_investment_return))
    cur.execute(query2)
    cur.execute("commit")    



def menushare():
 ch='y'
 while ch in 'Yy':
     print('*'*70)
     print('\t\t\t *  SHARE MARKET '," *")
     print('*'*70)
     print('\t\t1. CREATE NEW USER ACCOUNT ')
     print("\t\t2. SIGN IN YOUR ACCOUNT")
     print("\t\t3. INVEST YOUR MONEY")
     print('\t\t4. CHECK GROWTH OF ALL COMPANIES')
     print('\t\t5. ADMIN LOGIN')
     print('*'*70)
     
     choice=int(input("\t\t ENTER your choice:"))
     print('*'*70)
     if choice==1:
         createaccount()
     elif choice==2:
         login()
         print('*'*70)
         print("\t\t\tAccess Granted")
         menushare()
         break
     elif choice==3:
         investment()
     elif choice==4:
         graphical_growth()
     elif choice==5:
         password="1234"
         passcode=(input("\t\t Enter the password:"))
         if passcode!=password:
             print("Sorry wrong password")
             break     
         print('*'*70)
         print('\t\t * WELCOME ADMIN  '," *")
         print('*'*70)
         print('\t\t 1.Update company share return ')
         print("\t\t 2.Insert new company")
         print("\t\t 3.delete a company")
         print("\t\t 4.EXIT()")
         print('*'*70)
         choice=int(input("\t\tEnter the choice :"))
         if choice==1:
             update()
         elif choice==2:
             insert()
         elif choice==3:
             delete()
         elif choice==4:
             exit()
     print('*'*70)
     ch=input("\t\t DO you want to continue(y/n):")
     print("*"*70)

menushare()



