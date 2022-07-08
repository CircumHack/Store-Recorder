import mysql.connector as mysql
from datetime import date,datetime
import random
import json

from numpy import byte
class Connect():
    def __init__(self,hostname='localhost',user='root',password='0SE3050K0SUN'):
        self.con = mysql.connect(host=hostname,user=user,password=password)
        self.con.autocommit=True
        self.cur = self.con.cursor()
        self.cur.execute('''USE store_recorder''')
        self.cur.execute('''SELECT ID FROM owner''')
        self.brownunique=[self.cur.fetchall()]
        self.cur.execute('''SELECT ID FROM branch''')
        self.brownunique.append(self.cur.fetchall())
        self.savelogin=False
        self.createownershop=False
        self.createauthchangepass=False
        self.changepass=False
        self.createcat=False
        self.createprod=False
        self.createbranch=False
        self.editprod=False
        self.delprod=False
        self.createrole=False
        self.editcat=False
        self.editrole=False
        self.delrole=False
        self.deleteslot=False
        self.createslot=False
        self.verifyemail=False
        self.reverifyemail=False
        self.verifyphone=False
        self.createworker=False
        self.createrecruit=False
        self.sendapplication=False
        self.editshop=False
        self.edituser=False
        self.con.commit()                   
    def create_person_shop_emp(self,person:list,shop:list,type:str,username:str,phnum:str,email:str):
        try:
            self.cur.execute('''SELECT Phone_Number,Email FROM owner''')
            own_from_db=self.cur.fetchall()
            self.cur.execute('''SELECT Phone_Number,Email FROM employee''')
            emp_from_db=self.cur.fetchall()
            self.cur.execute('''SELECT Username FROM owner WHERE Username="%s" '''%username)
            own_ere=sorted(set(sum(self.cur.fetchall(),())))
            self.cur.execute('''SELECT Username FROM employee WHERE Username="%s" '''%username)
            emp_ere=sorted(set(sum(self.cur.fetchall(),())))
            all_ere=own_ere+emp_ere
            if len(all_ere)==0:
                usern=username
            else:
                self.cur.execute(f'''SELECT Username FROM owner WHERE Username="{username}" OR Username REGEXP "{username}[1-9]+"''')
                own_start=sum(self.cur.fetchall(),())
                self.cur.execute(f'''SELECT Username FROM employee WHERE Username="{username}" OR Username REGEXP "{username}[1-9]+"''')
                emp_start=sum(self.cur.fetchall(),())
                s=list(map(lambda i:i.removeprefix(username),own_start+emp_start))
                if '' in s:
                    s.remove('')
                s=list(map(int,s))
                if s==[]:
                    usern=username+'1'
                else:
                    usern=username+str(max(s)+1)                
            for i in own_from_db+emp_from_db:
                if phnum in i or email in i:
                    return 'User already exists',None
            if type=='Owner':
                self.cur.execute('''SELECT Shop_ID FROM owner WHERE ID="%s"'''%person[0])
                cu=sum(self.cur.fetchall(),())
                self.cur.execute('''SELECT ID FROM branch WHERE Owner_ID="%s"'''%person[0])
                cb=sum(self.cur.fetchall(),())
                self.cur.execute('''SELECT Email FROM branch WHERE ID="%s" OR Email="%s"'''%(shop[0],shop[5]))
                ww=sum(self.cur.fetchall(),())
                if shop[0] in cu or shop[0] in cb or shop[5] in ww:
                    return 'You can not duplicate Existing Shop',None
                else:
                    sid=self.stop_collision_id(shop[0],'Shop')
                    pid=self.stop_collision_id(person[0],'Personal')
                    p=[pid,person[1],person[2],person[3],sid,person[4],person[5],person[6],person[7],person[8],person[9],usern,person[10],person[11],person[12]]
                    s=[sid,shop[1],shop[2],shop[3],shop[4],pid,shop[5],shop[6],shop[7],shop[8],shop[9]]
                    ins=[
                        '''INSERT INTO owner(ID,Name,Gender,DOB,Shop_ID,Account_Picture_URL,Home_Address,State_City,Country,Phone_Number,Email,Username,Password,Devices,Currency,Date_of_Creation)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())''',
                        '''INSERT INTO branch(ID,Name,Shop_Address,State_City,Country,Owner_ID,Email,Phone_Number,Type,Account_Picture_URL,Currency,Date_of_Creation,Roles) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),{"MYSBUY2316621138": ["Buyer", "He/She is in charge of purchase or restocking products in the shop",0, 0], "MYSCAS23164550322863": ["Cashier", "He/She is responsible for receiving and documenting payments for products",0,0], "MYSCUS23164445555923153516054555231647352316095914321163": ["Customer Service Provider", "He/She provides help services to customers before, during and after a purchase both online and offline", 0,0], "MYSINV3214324519284505165247351959231403596335622359140316550337": ["Inventory Control Specialists", "He/She is in charge of the supply and storage and accessibility of items in order to ensure adequate supply without excessive oversupply", 0, 0], "MYSSAL0359322316523216192847": ["Salesperson", "He/She represents a shop and sells the company's product or services",0, 0]})'''
                    ]
                    self.cur.execute('''SELECT Name FROM branch WHERE Owner_ID="%s" '''%pid)
                    yt=sum(self.cur.fetchall(),())
                    if shop[1] not in yt:
                        self.cur.execute(ins[0],p)
                        self.cur.execute(ins[1],s)
                        self.createownershop=True
                        self.type='Owner'
                        self.track(p,s)
                        return 'Done',usern
                    else:
                        return 'The shop is already owned by You',None
            elif type=='Recruit':                        
                self.cur.execute('''SELECT ID FROM recruit WHERE Email="%s" OR Phone_Number="%s" '''%(email,phnum))
                rec_id=sum(self.cur.fetchall(),())
                if len(rec_id)==0:
                    pid=self.stop_collision_id(person[0],'Personal')
                    p=[pid,person[1],person[2],person[3],person[4],person[5],person[6],person[7],person[8],person[9],person[10],person[11],person[12],person[13]]
                    s=[shop[0],shop[1],datetime.now()]#VACANCY ->Code,Documents,Date,
                    self.cur.execute('''INSERT INTO recruit(Vacancy,ID,Name,Gender,DOB,Picture_URL,Home_Address,State_City,Country,Phone_Number,Email,Username,Password,Devices,Currency,Date_of_Creation) 
                    VALUES ({s[0]:[s[1],s[2]]},%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())''',p)
                    self.createrecruit=True
                    self.type='Recruit'
                    self.track(p,s) 
                    return 'Done'
                else:
                    if len(rec_id)==1:
                        self.cur.execute('''SELECT Vacancy FROM recruits WHERE ID="%s" '''%rec_id[0])
                        r=sum(self.cur.fetchall(),())[0]
                        vac=json.loads(r)
                        if shop[0] not in vac:
                            n=datetime.now()
                            vac[shop[0]]=[shop[1],n]
                            self.cur.execute('''UPDATE recruit SET Vacancy="%s" WHERE ID="%s" '''%(vac,rec_id[0]))
                            self.sendapplication=True
                            self.type='Recruit'
                            self.track(person[0],person[1],shop[0],shop[1])
                            return 'Done'
                        return 'Vacancy Application exists'
                    return 'Recruit Account already exists'
        except:
            return 'Check your internet connection'
    def stop_collision_id(self,id:str,type:str):
        id=id.replace(' ','')
        if type=='Personal':
            self.cur.execute('''SELECT ID FROM owner WHERE ID="%s" '''%id)
            o=sum(self.cur.fetchall(),())
            self.cur.execute('''SELECT ID FROM employee WHERE ID="%s" '''%id)
            e=sum(self.cur.fetchall(),())
            if id in e+o:
                while True:
                    s=str(random.randint(1000,9999))
                    self.cur.execute('''SELECT ID FROM owner WHERE ID="%s" '''%id[:-4]+s)
                    o=sum(self.cur.fetchall(),())
                    self.cur.execute('''SELECT ID FROM employee WHERE ID="%s" '''%id[:-4]+s)
                    e=sum(self.cur.fetchall(),())
                    if id[:-4]+s not in e+o:
                        id=id[:-4]+s
                        break
        elif type=='Shop':
            self.cur.execute('''SELECT ID FROM branch WHERE ID="%s" '''%id)
            o=sum(self.cur.fetchall(),()) 
            if id in o:
                while True:
                    s=str(random.randint(1000,9999))
                    self.cur.execute('''SELECT ID FROM branch WHERE ID="%s" '''%id[:-4]+s)
                    o=sum(self.cur.fetchall(),()) 
                    if id[:-4]+s not in o:
                        id=id[:-4]+s
                        break
        elif type=='Category':
            self.cur.execute('''SELECT Category FROM branch''')
            o=sum(self.cur.fetchall(),()) 
            js=[]
            for i in o:                
                try:
                    r=json.loads(i)
                    for j in r:
                        js.append(j)
                except:
                    pass                
            if id in js:
                while True:
                    s=str(random.randint(1000,9999))
                    if id[:-4]+s not in js:
                        id=id[:-4]+s
                        break
        elif type=='Roles':
            self.cur.execute('''SELECT Roles FROM branch''')
            o=sum(self.cur.fetchall(),()) 
            js=[]
            for i in o:                
                try:
                    r=json.loads(i)
                    for j in r:
                        js.append(j)
                except:
                    pass                
            if id in js:
                while True:
                    s=str(random.randint(1000,9999))
                    if id[:-4]+s not in js:
                        id=id[:-4]+s
                        break
        elif type=='Product':
            self.cur.execute('''SELECT ID FROM product WHERE ID="%s" '''%id)
            o=sum(self.cur.fetchall(),()) 
            if id in o:
                while True:
                    s=str(random.randint(1000,9999))
                    self.cur.execute('''SELECT ID FROM product WHERE ID="%s" '''%id[:-4]+s)
                    o=sum(self.cur.fetchall(),()) 
                    if id[:-4]+s not in o:
                        id=id[:-4]+s
                        break
        elif type=='Vacancy':
            self.cur.execute('''SELECT Vacancy_Code FROM employ_records WHERE Vacancy_Code="%s"'''%id)
            o=sum(self.cur.fetchall(),())
            if id in o:
                while True:
                    s=str(random.randint(1000,9999))
                    self.cur.execute('''SELECT Vacancy_Code FROM employ_records WHERE Vacancy_Code="%s"'''%id[:-4]+s)
                    o=sum(self.cur.fetchall(),())
                    if id[:-4]+s not in o:
                        id=id[:-4]+s
                        break
        return id        
    def track(self,*data):
        if self.createownershop:            
            d=[f'Creation of New Owner with Name:{data[0][1]},Personal ID:{data[0][0]},Gender:{data[0][2]},Date of Birth:{data[0][3]},Personal Email Address:{data[0][10]},Personal Phone Number:{data[0][9]},User_Picture_URL:{data[0][5]},Home Address: Street->({data[0][6]}) State/City->({data[0][7]}) Country->({data[0][8]}), Currency:{data[0][14]},Device Used:{data[0][13]},Shop ID:{data[1][0]},Shop Name:{data[1][1]},Shop Adrress: Street->({data[1][2]}) State/City->({data[1][3]}) Country->({data[1][4]}),CEO:True,Shop Email Address:{data[1][6]},Shop Phone Number:{data[1][7]},Shop Type:Headquaters, Shop Picture:{data[1][9]}, Shop Currency:{data[1][10]}',
                data[0][0],
                self.type
            ]
            self.createownershop=False
        elif self.createrecruit:
            d=[f'Creation of New Recruit with Name:{data[0][1]},Personal ID:{data[0][0]},Gender:{data[0][2]},Date of Birth:{data[0][3]}, Email Address:{data[0][9]},Phone Number:{data[0][8]},Picture URL:{data[0][4]},Home Address: Street->({data[0][5]}) State/City->({data[0][6]}) Country->({data[0][7]}), Currency:{data[0][13]},Device Used:{data[0][12]}, Vacancy Code:{data[1][0]}, Douments URLs:{data[1][1]}, Date of Application:{data[1][2]}',
                data[0][0],
                self.type    
            ]
            self.createrecruit=False
        elif self.createauthchangepass:
            d=[f'User with ID {data[0]} attempted to change password. The access key is {data[1]}',
                data[0],
                self.type
            ]
            self.createauthchangepass=False
        elif self.changepass:
            d=[f'User with ID {data[0]} changed Password using access key {data[1]}.',
               data[0],
               self.type
            ]
            self.changepass=False
        elif self.createcat:
            d=[f'User with ID:{data[0]} used Shop with ID:{data[1]} to create a Product Category {data[2]} that has ID {data[3]}',
                data[0],
                self.type
            ]
            self.createcat=False
        elif self.createrole:            
            d=[f'User with ID:{data[0]} created Role {data[1]} which ID is {data[2]} in Shop with ID: {data[3]} and Salary: {data[4]}',
               data[0],
               self.type                
            ]
            self.createrole=False
        elif self.createprod:            
            d=[f'User with ID:{data[0]} created Product {data[1]} which ID is {data[2]}, Type is {data[3]} and Unit Price is {data[4]} in Category with ID:{data[5]} and Supplier Shop ID is {data[6]}',
                data[0],
                self.type                
            ]
            self.createprod=False            
        elif self.editprod:
            d=[data[0],
               data[1],
               self.type
            ]
            self.editprod=False
        elif self.delprod:
            d=[data[0],
               data[1],
               self.type
            ]
            self.delprod=False        
        elif self.editcat:
            d=[data[0],
               data[1],
               self.type
            ]
            self.editcat=False
        elif self.delrole:
            d=[data[0],
               data[1],
               self.type                
            ]
            self.delrole=False
        elif self.createslot:
            d=[f'{data[0]} created {data[3]} slot(s) in Shop with ID {data[1]}, Role with ID {data[2]} from {data[4]} to {data[5]}',
               data[0],
               self.type
            ]
            self.createslot=False
        elif self.deleteslot:
            d=[f'{data[0]} slots with Shop_ID {data[1]}, Department_ID: {data[2]}, Level: {data[3]} expired on {data[4]}.'
                'System',
                self.type
            ]
            self.deleteslot=False
        elif self.savelogin:
            d=[f'{data[0]} logged in Shop with ID {data[1]}.',
                data[0],
                self.type
            ]
            self.savelogin=False            
        elif self.verifyemail:
            d=[f'{data[2]}: {data[0]} generated a verification code {data[1]}',
                'System',
                self.type
            ]
            self.verifyemail=False
        elif self.reverifyemail:
            d=[f'{data[2]}: {data[0]} regenerated a verification code {data[1]}',
                'System',
                self.type                
            ]
            self.reverifyemail=False
        elif self.editrole:
            d=[data[0],
                data[1],
                self.type
            ]
            self.editrole=False
        elif self.sendapplication:
            d=[f'Recruit {data[1]} ({data[0]}) submitted an application to Vacancy Code ({data[2]}), Documents URL ({data[3]})',
                'System',
                self.type
            ]
            self.sendapplication=False
        elif self.editshop:
            d=[f'Shop with ID: {data[1]} was edited with format '+str({"Field":["Old","New"]})+f'  ---->>>   {str(data[0])}',
               data[1],
               self.type               
            ]
            self.editshop=False
        elif self.edituser:
            d=[f'User with ID: {data[1]} was edited with format '+str({"Field":["Old","New"]})+f'  ---->>>   {str(data[0])}',
               data[1],
               self.type               
            ]
            self.edituser=False
        ins='''INSERT INTO activities(Date_and_Time,Activity,User_ID,Type) VALUES (NOW(),"%s","%s","%s")''' % (d[0],d[1],d[2])
        self.cur.execute(ins)
        self.con.commit()
    def get_shop(self,userid):
        self.cur.execute('''SELECT Name,Shop_Address,Email,Type FROM branch WHERE Owner_ID="%s" '''%userid)        
        return self.cur.fetchall()
    def getuser(self,user:str,shopid:str):
        self.cur.execute('''SELECT ID FROM owner WHERE Shop_ID!="%s" AND (Username="%s" OR ID="%s") '''%(shopid,user,user))
        return list(set(sum(self.cur.fetchall(),())))
    def getshop(self,emailid:str):
        self.cur.execute('''SELECT ID FROM branch WHERE Email="%s" OR ID="%s" '''%(emailid,emailid))        
        return list(set(sum(self.cur.fetchall(),())))
    def getpic(self,id):
        self.cur.execute('''SELECT Account_Picture DUMP''')
    def search_user_email(self,useremail=''):
        self.cur.execute('''SELECT Password FROM owner WHERE Username="%s" OR Email="%s"'''%(useremail,useremail))
        f=sum(self.cur.fetchall(),())
        type=None
        if len(f)>0:
            type='Owner'
        elif len(f)==0:
            self.cur.execute('''SELECT Password FROM employee WHERE Username="%s" OR Email="%s"'''%(useremail,useremail))
            f=sum(self.cur.fetchall(),())
            if len(f)>0:
                type='Employee'
        return f,type
    def get_shop_id_from_userid(self,userid:str,type:str):
        if type=='Owner':
            self.cur.execute('''SELECT Shop_ID FROM owner WHERE ID="%s" '''%userid)
            f=sum(self.cur.fetchall(),())
        elif type=='Employee':
            self.cur.execute('''SELECT Shop_ID FROM employee WHERE ID="%s" '''%userid)
            f=sum(self.cur.fetchall(),())
        return f
    def get_userid(self,useremail,password,type):
        if type=='Owner':
            self.cur.execute('''SELECT ID FROM owner WHERE Password="%s" AND (Username="%s" OR Email="%s") '''%(password,useremail,useremail))
            f=sum(self.cur.fetchall(),())
        elif type=='Employee':
            self.cur.execute('''SELECT ID FROM employee WHERE Password="%s" AND (Username="%s" OR Email="%s") '''%(password,useremail,useremail))
            f=sum(self.cur.fetchall(),())
        return f
    def get_device(self,adr:str):
        self.cur.execute('''SELECT Devices FROM owner''')
        d=sum(self.cur.fetchall(),())
        for i in d:
            if adr in i:
                return True
        return False
    def get_user_email(self,fue):
        self.cur.execute('''SELECT Username FROM owner WHERE Username="%s" OR Email="%s"'''%(fue,fue))
        ans=sum(self.cur.fetchall(),())
        if len(ans)!=1:
            self.cur.execute('''SELECT Username FROM employee WHERE Username="%s" OR Email="%s"'''%(fue,fue))
            ans=sum(self.cur.fetchall(),())
            if len(ans)!=1:
                self.cur.execute('''SELECT Username FROM recruit WHERE Username="%s" OR Email="%s"'''%(fue,fue))
                ans=sum(self.cur.fetchall(),())
        return ans
    
    def ins_change_user_pass(self,useremail:str,auth:str):
        self.cur.execute('''SELECT ID FROM employee WHERE (Username="%s" OR Email="%s")'''%(useremail,useremail))
        b=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT ID FROM owner WHERE (Username="%s" OR Email="%s")'''%(useremail,useremail))
        d=sum(self.cur.fetchall(),())
        n='''SELECT Valid FROM user_password_changer WHERE UserID="%s"'''
        et='''DELETE FROM user_password_changer WHERE TIMESTAMPDIFF(MINUTE,DateTime,NOW()) > 15 OR Valid=0'''
        self.cur.execute(et)
        self.con.commit()
        s='''INSERT INTO user_password_changer(DateTime,UserID,auth) VALUES (NOW(),"%s","%s")'''
        state=False
        if len(b)==1:
            self.cur.execute(n%b[0])
            e=sum(self.cur.fetchall(),())
            if len(e)==0 :
                do=True
            elif e[-1]==False:
                do=True
            else:
                do=False
            if do:
                self.cur.execute(s,(b[0],auth))
                self.type='Employee'
                self.cpid=b[0]
                self.createauthchangepass=True
                self.track(b[0],auth)
        elif len(d)==1:
            self.cur.execute(n%d[0])
            e=sum(self.cur.fetchall(),())
            if len(e)==0 :
                do=True
            elif e[-1]==False:
                do=True
            else:
                do=False
            if do:
                self.cur.execute(s%(d[0],auth))
                self.type='Owner'
                self.cpid=d[0]
                self.createauthchangepass=True
                self.track(d[0],auth)
    def change_pass(self,access:str,newpass:str,useremail:str):
        self.cur.execute('''SELECT ID FROM employee WHERE Username="%s" OR Email="%s"'''%(useremail,useremail))
        b=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT ID FROM owner WHERE Username="%s" OR Email="%s"'''%(useremail,useremail))
        d=sum(self.cur.fetchall(),())
        if len(b)>=1:
            self.cpid=b[-1]
            s='''UPDATE employee SET Password="%s" WHERE ID="%s"'''%(newpass,self.cpid)
            self.type='Employee'
        elif len(d)>=1:
            self.cpid=d[-1]
            s='''UPDATE owner SET Password="%s" WHERE ID="%s" '''%(newpass,self.cpid)
            self.type='Owner'
        else:
            return False
        self.cur.execute('''SELECT auth FROM user_password_changer WHERE UserID="%s"'''%self.cpid)
        ree=sum(self.cur.fetchall(),())
        if access in ree:
            self.cur.execute(s)
            self.changepass=True
            self.cur.execute('''UPDATE user_password_changer SET Valid=0 WHERE UserID="%s" AND auth="%s" '''%(self.cpid,access))
            self.track(self.cpid,access)
            self.con.commit()
    def create_cat(self,data):
        self.cur.execute('''SELECT Category FROM branch WHERE ID="%s"'''%data[3])
        new=sum(self.cur.fetchall(),())
        cid=self.stop_collision_id(data[0],'Category')
        name=[]
        for i in new:
            try:
                js=json.loads(i)
                if js:
                    for i in js:
                        name.append(js[i][0])
            except:
                js={}            
        if data[1] not in name:              
            js.update({cid:[data[1],data[2],data[5]]})                 
            js=json.dumps(js)
            self.cur.execute("""UPDATE branch SET Category='%s' WHERE ID="%s" """%(js,data[3]))
            self.createcat=True
            self.type='Owner'
            self.track(data[4],data[3],data[1],cid)
            self.con.commit()
            return 'Done',cid
        return 'Already Exists',cid
    def create_role(self,data):        
        self.cur.execute('''SELECT Roles FROM branch WHERE ID="%s"'''%data[4])
        new=sum(self.cur.fetchall(),())
        rid=self.stop_collision_id(data[0],'Roles')
        name=[]
        for i in new:
            try:
                js=json.loads(i)
                if js:
                    for i in js:
                        name.append(js[i][0])
            except:
                js={}            
        if data[1] not in name:              
            js.update({rid:[data[1],data[2],data[3],data[6]]})                 
            js=json.dumps(js)
            self.cur.execute("""UPDATE branch SET Roles='%s' WHERE ID="%s" """%(js,data[4]))
            self.createrole=True
            self.type='Owner'
            self.track(data[5],data[1],data[0],data[4],data[3])
            self.con.commit()
            return 'Done',rid
        return 'Already Exists',rid
    def check_prod(self,pid,sid):
        if pid=='':
            return False
        else:
            self.cur.execute('''SELECT ID FROM category WHERE Shop_ID="%s"'''%sid)
            b=sum(self.cur.fetchall(),())
            for i in b:
                self.cur.execute('''SELECT ID,Name FROM product WHERE Category_ID="%s" AND (ID="%s" OR Name="%s")'''%(i,pid,pid))
                a=sum(self.cur.fetchall(),())
                if len(a)==1:
                    return True
            return False
    def create_prod(self,*data):        
        self.cur.execute('''SELECT Name FROM product WHERE Category_ID="%s" AND Type="%s"'''%(data[5],data[2]))
        new=sum(self.cur.fetchall(),())
        pid=self.stop_collision_id(data[0],'Product')
        if data[1] not in new:            
            self.cur.execute('''SELECT Category FROM branch WHERE ID="%s"'''%data[9])
            a=sum(self.cur.fetchall(),())[0]
            try:
                s=json.loads(a)
                s[data[5]]=[s[data[5]][0],s[data[5]][1],s[data[5]][2]+1]
            except:
                s={}
            if s!={}:
                self.cur.execute('''INSERT INTO product(ID,Name,Type,Unit_Price,Measure,Category_ID,Description,Supplier_Shop_ID,Date_of_Creation) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s",NOW())'''%(pid,data[1],data[2],data[3],data[4],data[5],data[6],data[7]))            
                self.cur.execute('''SELECT No_of_Products FROM branch WHERE ID="%s"'''%data[9])            
                a=sum(self.cur.fetchall(),())[0]
                s=json.dumps(s)
                self.cur.execute("""UPDATE branch SET Category='%s', No_of_Products="%s" WHERE ID="%s" """%(s,a+1,data[9]))                
                self.createprod=True
                self.type='Owner'
                self.track(data[8],data[1],data[0],data[2],data[3],data[5],data[7])
                self.con.commit()
            return 'Done',pid
        return 'Product already exists',None
    def edit_prod(self,pid,uid,edidict:dict,pastdict:dict,quan_reason=''):
        s=False
        for i in edidict:
            if edidict[i]!=pastdict[i]:
                s=True
                break    
        if s:
            m=f'{uid} edited Product {pastdict["Name"]} ({pid}) by changing '        
            if edidict['Name']!=pastdict['Name']:
                i=edidict['Name'][:4].upper()
                self.cur.execute('''UPDATE product SET Name="%s" WHERE ID="%s" '''%(edidict['Name'],pid))
                npid=self.stop_collision_id(pid[:3]+i+pid[7:],'Product')
                self.cur.execute('''UPDATE product SET ID="%s" WHERE ID="%s" '''%(npid,pid))            
                m+=f'Name from {pastdict["Name"]} to {edidict["Name"]}, ID from {pid} to {pid[:3]+i+pid[7:]}, '
                pid=npid
            if edidict['Price']!=pastdict['Price']:
                self.cur.execute('''UPDATE product SET Unit_Price="%s" WHERE ID="%s" '''%(edidict['Price'],pid))
                m+=f'Unit Price from {pastdict["Price"]} to {edidict["Price"]}, '
            if edidict['Measure']!=pastdict['Measure']:
                self.cur.execute('''UPDATE product SET Measure="%s" WHERE ID="%s" '''%(edidict['Measure'],pid))
                m+=f'Measure from {pastdict["Measure"]} to {edidict["Measure"]}, '
            if edidict['Quantity']!=pastdict['Quantity']:
                self.cur.execute('''UPDATE product SET Quantity="%s" WHERE ID="%s" '''%(edidict['Quantity'],pid))
                m+=f'Quantity from {pastdict["Quantity"]} to {edidict["Quantity"]} with Reasons: {quan_reason}, '
            if edidict['CID']!=pastdict['CID']:
                self.cur.execute('''SELECT ID FROM category  WHERE ID="%s" '''%edidict['CID'])
                if sum(self.cur.fetchall(),())==1:
                    self.cur.execute('''UPDATE product SET Category_ID="%s" WHERE ID="%s" '''%(edidict['CID'],pid))
                    m+=f'Category ID from {pastdict["CID"]} to {edidict["CID"]}, '
            if edidict['Desc']!=pastdict['Desc']:
                self.cur.execute('''UPDATE product SET Description="%s" WHERE ID="%s" '''%(edidict['Desc'],pid))
                m+=f'Description from {pastdict["Desc"]} to {edidict["Desc"]}, '
            if edidict['SHID']!=pastdict['SHID']:
                self.cur.execute('''UPDATE product SET Supplier_Shop_ID="%s" WHERE ID="%s" '''%(edidict['SHID'],pid))    
                m+=f'Supplier ID from {pastdict["SHID"]} to {edidict["SHID"]}, '
            m=m[:-2]+'.'
            self.type='Owner'
            self.editprod=True
            self.track(m,uid)
            self.con.commit()
            return 'Done'
        return 'No Change Made'
    def get_prod(self,idname:str,category):        
        self.cur.execute('''SELECT Name,Type,Unit_Price,Measure,Quantity,Category_ID,Description,Supplier_Shop_ID,ID FROM product WHERE ID="%s" OR Name="%s" '''%(idname,idname))
        w=self.cur.fetchall()
        if len(w)==1:
            w=sum(w,())
            try:
                return w[0],f'Type: {str(w[1])[2:-2]}',w[2],w[3],w[4],category[w[5]][0],w[6],w[7],w[8]
            except:
                return False
        return False
    def del_prod(self,pnamid,reas,sid,uid):
        w=None
        self.cur.execute('''SELECT Category_ID FROM product WHERE Name="%s" OR ID="%s" '''%(pnamid,pnamid))
        c=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Category FROM branch WHERE ID="%s"'''%sid)
        a=sum(self.cur.fetchall(),())
        try:
            s=json.loads(a[0])
            s[c[0]]=[s[c[0]][0],s[c[0]][1],s[c[0]][2]-1]
        except:
            s={}
        if len(c)==1 and s!={}:
            self.cur.execute('''SELECT Name,ID,Quantity,Measure FROM product WHERE Category_ID="%s" AND (Name="%s" OR ID="%s")'''%(c[0],pnamid,pnamid))
            v=sum(self.cur.fetchall(),())
            if len(v)==4:
                if int(v[2])==0:                        
                    s=json.dumps(s)
                    self.cur.execute('''SELECT No_of_Products FROM branch WHERE ID="%s"'''%sid)
                    w=int(sum(self.cur.fetchall(),())[0])
                    self.cur.execute("""UPDATE branch SET Category='%s', No_of_Products="%s" WHERE ID="%s" """%(s,w-1,sid))
                    self.cur.execute('''DELETE FROM product WHERE Category_ID="%s" AND (Name="%s" OR ID="%s")'''%(c[0],pnamid,pnamid))                
                    m=f'{uid} deleted Product {v[0]} with ID {v[1]} in Category with ID {c[0]} with Reasons as -->> ({reas})'
                    self.cur.execute('''SELECT No_of_Products FROM branch WHERE ID="%s"'''%sid)
                    w=int(sum(self.cur.fetchall(),())[0])
                    self.delprod=True
                    self.type='Owner'
                    self.track(m,uid)
                    self.con.commit()
                    return 'Deleted',w
                else:
                    return f'There are still {w[3]} {w[4]}(s) of {w[0]} left',w                
        return f'Product {pnamid} does not exists',w        
    def edit_cat(self,uid,bid,cid,edidict:dict,pastdict:dict):
        m=f'{uid} edited Category {pastdict["Name"]} ({cid}) by changing '
        self.cur.execute('''SELECT Category FROM branch WHERE ID="%s"'''%bid)
        s=sum(self.cur.fetchall(),())[0]
        try:
            v=json.loads(s)
            s={}
            old=v[cid]
            for i in v:
                if i!=cid:
                    s[i]=v[i]
        except:
            s=None
        if s!=None:
            if edidict!={}:
                if 'Name' in edidict:
                    i=edidict['Name'][:3].upper()                
                    old[0]=edidict['Name']
                    oid=cid
                    cid=self.stop_collision_id(cid[:3]+i+cid[6:],'Category')                
                    m+=f'Name from {pastdict["Name"]} to {edidict["Name"]}, ID from {oid} to {cid}, '
                if 'Desc' in edidict:
                    old[1]=edidict['Desc']
                    m+=f'Description from {pastdict["Desc"]} to {edidict["Desc"]}, '
                s[cid]=old
                s=json.dumps(s)
                self.cur.execute("""UPDATE branch SET Category='%s' WHERE ID="%s" """%(s,bid))
                m=m[:-2]+'.'
                self.type='Owner'
                self.editcat=True
                self.track(m,uid)
                self.con.commit()
                return 'Done',cid
        return 'Empty',cid
    def edit_role(self,uid,bid,rid,edidict:dict,pastdict:dict):
        m=f'{uid} edited Role {pastdict["Name"]} ({rid}) by changing '
        self.cur.execute('''SELECT Roles FROM branch WHERE ID="%s"'''%bid)
        s=sum(self.cur.fetchall(),())[0]
        try:
            v=json.loads(s)
            s={}
            old=v[rid]
            for i in v:
                if i!=rid:
                    s[i]=v[i]
        except:
            s=None
        if s!=None:
            if edidict!={}:
                if 'Name' in edidict:
                    i=edidict['Name'][:3].upper()                
                    old[0]=edidict['Name']
                    oid=rid
                    rid=self.stop_collision_id(rid[:4]+i+rid[6:],'Roles')                
                    m+=f'Name from {pastdict["Name"]} to {edidict["Name"]}, ID from {oid} to {rid}, '
                    for i in v:
                        if v[i][0]==edidict['Name']:
                            return 'Error',oid
                if 'Desc' in edidict:
                    old[1]=edidict['Desc']
                    m+=f'Description from {pastdict["Desc"]} to {edidict["Desc"]}, '
                if 'Salary' in edidict:
                    old[2]=edidict['Salary']
                    m+=f'Salary from {pastdict["Salary"]} to {edidict["Salary"]}, '
                s[rid]=old
                s=json.dumps(s)
                self.cur.execute("""UPDATE branch SET Roles='%s' WHERE ID="%s" """%(s,bid))
                m=m[:-2]+'.'
                self.type='Owner'
                self.editrole=True
                self.track(m,uid)
                self.con.commit()
                return 'Done',rid
        return 'Empty',rid
    def del_cat(self,cid,reas,sid,uid):
        self.cur.execute('''SELECT Category FROM branch WHERE ID="%s"'''%sid)
        c=sum(self.cur.fetchall(),())
        if len(c)==1:
            try:
                v=json.loads(c[0])
                s={}
                for i in v:
                    if i!=cid:
                        s[i]=v[i]                                    
            except:
                s=None     
            if s!=None:                
                if v[cid][2]<1:
                    self.cur.execute("""UPDATE branch SET Category='%s' WHERE ID="%s" """%(s,sid))
                    m=f'{uid} deleted Category {v[cid][0]} with ID {cid} in Shop with ID {sid} with Reasons as {reas}.'
                    self.delcat=True
                    self.type='Owner'
                    self.track(m,uid)
                    self.con.commit()
                    return 'Deleted'
                else:
                    return f'Category with ID: {cid} is not empty'
        return f'Category with {cid} does not exists'
    def del_role(self,rid,reas,sid,uid):
        self.cur.execute('''SELECT Roles FROM branch WHERE ID="%s"'''%sid)
        c=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Number_of_Slots FROM employ_records WHERE Role_ID="%s" AND Shop_ID="%s"'''%(rid,sid))
        vacempty=False
        num=sum(self.cur.fetchall(),())
        if len(num)==0:
            vacempty=True
        else:
            if num[0]==0:
                vacempty=True
        if len(c)==1:
            try:
                v=json.loads(c[0])
                s={}
                for i in v:
                    if i!=rid:
                        s[i]=v[i]                                    
            except:
                s=None     
            if s!=None:                
                s=json.dumps(s)
                if v[rid][3]<1 and vacempty:
                    self.cur.execute("""UPDATE branch SET Roles='%s' WHERE ID="%s" """%(s,sid))
                    m=f'{uid} deleted Role {v[rid][0]} with ID {rid} in Shop with ID {sid} with Reasons as {reas}.'
                    self.delrole=True
                    self.type='Owner'
                    self.track(m,uid)
                    self.con.commit()
                    return 'Deleted'
                else:
                    return f'Role with ID: {rid} is not empty'
        return f'Role with {rid} does not exists'
    def delete_slot(self,date):
        self.cur.execute('''SELECT Department_ID,Level,Number_of_Slots,End_Date FROM employ_records WHERE End_Date<="%s" '''%date)
        s=self.cur.fetchall()
        self.cur.execute('''DELETE FROM employ_records WHERE End_Date<"%s" '''%date)
        self.deleteslot=True
        self.owner='System'
        for i in s:
            self.track(i[3],i[0],i[1],i[2],i[4])
    def create_slot(self,data:list):
        self.cur.execute('''SELECT Number_of_Slots FROM employ_records WHERE Role_ID="%s" AND Shop_ID="%s"'''%(data[0],data[2]))
        r=sum(self.cur.fetchall(),())
        if len(r)==1:
            s=int(r[0])+int(data[1])
            self.cur.execute('''UPDATE employ_records SET Number_of_Slots="%s" WHERE Role_ID="%s" '''%(s,data[0]))
            self.cur.execute('''UPDATE employ_records SET End_Date="%s" WHERE Role_ID="%s" '''%(data[5],data[0]))
        elif len(r)==0:
            vac=self.stop_collision_id(data[6],'Vacancy')            
            self.cur.execute('''INSERT INTO employ_records(Date_of_Creation,Role_ID,Number_of_Slots,Start_Date,End_Date,Vacancy_Code,Shop_ID) VALUES (NOW(),"%s","%s","%s","%s","%s","%s")'''%(data[0],data[1],data[4],data[5],vac,data[2]))
        else:
            return 'Error'
        self.createslot=True
        self.type='Owner'        
        self.track(data[3],data[2],data[0],data[1],data[4].ctime(),data[5].ctime())
        return 'Done'
    def del_branch(self,data:list):
        self.cur.execute('''DELETE FROM branch WHERE Owner_ID="%s" AND (ID="%s" OR Name="%s")''')
    def join_dep(self,sid):
        self.cur.execute('SELECT Department FROM branch WHERE ID="%s"'%sid)
        a=self.cur.fetchall()
        if a!=[]:
            self.cur.execute('''SELECT Levels FROM department WHERE ID="%s"''')
    def search_shop_vac(self,vid):
        now=datetime.today()
        self.delete_slot(now)
        self.cur.execute('''SELECT Department_ID,Level,Start_Date,End_Date,Number_of_Slots FROM employ_records WHERE Vacancy_Code="%s"'''%vid)
        val=sum(self.cur.fetchall(),()) 
        if len(val)!=0:
            self.cur.execute('''SELECT Name,Shop_ID,Levels FROM department WHERE ID="%s"'''%val[0])                    
            d=sum(self.cur.fetchall(),())
            l=json.loads(d[2])            
            if len(d)!=0:
                self.cur.execute('''SELECT Name,Currency FROM branch WHERE ID="%s"'''%d[1])
                s=sum(self.cur.fetchall(),())
                f=val[2].ctime().split()
                e=val[3].ctime().split()
                if len(s[0])>10:
                    s[0]=s[0][:10]+'...'
                if len(d[0])>16:
                    dname=d[0][:16]+'...'
                else:
                    dname=d[0]
                if len(l[str(val[1])][0])>25:
                    lnam=l[str(val[1])][0][:22]+'...'
                else:
                    lnam=l[str(val[1])][0]
                return [s[0],dname,lnam,f'{s[1]} {l[str(val[1])][1]} {l[str(val[1])][2]}',f'{f[1]} {f[2]}, {f[4]} to {e[1]} {e[2]}, {e[4]}']
        return 'Vacancy does not exists'
    def verify_email_phone(self,emailphone,code,type_data,retry=False):
        self.cur.execute('''DELETE FROM verifyemailphone WHERE Type="Email" AND (TIMESTAMPDIFF(MINUTE,DateTime,NOW()) > 30 OR Validity=0)''')
        self.cur.execute('''DELETE FROM verifyemailphone WHERE Type="Phone" AND (TIMESTAMPDIFF(MINUTE,DateTime,NOW()) > 15 OR Validity=0)''')
        self.cur.execute('''SELECT Email FROM owner''')
        self.owner_email=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Email FROM employee''')
        self.employeee_email=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Email FROM recruit''')
        self.recruit_email=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Email FROM branch''')
        self.branch_email=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Phone_Number FROM owner''')
        self.owner_phone=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Phone_Number FROM employee''')
        self.employeee_phone=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Phone_Number FROM recruit''')
        self.recruit_phone=sum(self.cur.fetchall(),())
        self.cur.execute('''SELECT Phone_Number FROM branch''')
        self.branch_phone=sum(self.cur.fetchall(),())
        if emailphone in self.owner_email+self.branch_email+self.recruit_email+self.employeee_email+self.owner_phone+self.branch_phone+self.recruit_phone+self.employeee_phone:
            return f'{emailphone} is already linked to an existing account'
        self.cur.execute('''SELECT Email_Phone FROM verifyemailphone''')
        a=sum(self.cur.fetchall(),())        
        if emailphone not in a:
            self.cur.execute('''INSERT INTO verifyemailphone(DateTime,Email_Phone,Code,Type,Validity) VALUES (NOW(),"%s","%s","%s",True)'''%(emailphone,code,type_data))
            self.verifyemail=True
            self.type='System'            
            self.track(emailphone,code,type_data)
            return 'Done'
        elif retry:
            self.cur.execute('''UPDATE verifyemailphone SET Code="%s" WHERE Email_Phone="%s"'''%(code,emailphone))
            self.cur.execute('''UPDATE verifyemailphone SET DateTime=NOW() WHERE Email_Phone="%s"'''%emailphone)
            self.reverifyemail=True
            self.type='System'            
            self.track(emailphone,code,type_data)
            return 'Resent'
        return f'{type_data} is still valid'
    def check_verify_email_phone(self,emailphone,s):
        self.cur.execute('''SELECT * FROM verifyemailphone WHERE Email_Phone="%s" AND Code="%s"'''%(emailphone,s))
        a=self.cur.fetchall()
        if len(a)==1:
            self.cur.execute('''DELETE FROM verifyemailphone WHERE Validity=True AND Email_Phone="%s"'''%emailphone)
            return 'Done'
        return 'Invalid Verification Code'
    def get_date_verify_email_phone(self,emailphone):
        self.cur.execute('''SELECT DateTime FROM verifyemailphone WHERE Email_Phone="%s"'''%emailphone)        
        return sum(self.cur.fetchall(),())[0]
    def extract_code_mail(self,email):
        self.cur.execute('''SELECT Code FROM verifyemailphone WHERE Email_Phone="%s"'''%email)
        return sum(self.cur.fetchall(),())[0]
    def get_info_login(self,user_id,shop_id,type):
        if type=='Owner':
            self.cur.execute('''SELECT Name,Account_Picture_URL,Account_Number,Home_Address,State_City,Country,Phone_Number,Email,Username,Currency FROM owner WHERE ID="%s"'''%user_id)
            per=self.cur.fetchall()
            self.cur.execute('''SELECT Name,Shop_Address,State_City,Country,Account_Number,Email,Phone_Number,Type,Roles,Category,Account_Picture_URL,Revenue,Expenditure,Currency,No_of_Workers,No_of_Products FROM branch WHERE ID="%s"'''%shop_id)
            shp=self.cur.fetchall()            
            self.cur.execute('''SELECT Vacancy_Code,Role_ID,Number_of_Slots,Start_Date,End_Date FROM employ_records WHERE Shop_ID="%s"'''%shop_id)
            vac=self.cur.fetchall()
            vacdata={}
            for i in vac:
                vacdata[i[0]]=i[1:]
            if len(per)==1 and len(shp)==1:   
                try:
                    rol=json.loads(shp[0][8])
                except:
                    rol={}
                try:
                    cat=json.loads(shp[0][9])
                except:
                    cat={}
                return {'Personal Name':per[0][0],'Account Picture':per[0][1],'Personal Home Address':per[0][3],'Personal State/City':per[0][4],'Personal Country':per[0][5],'Personal Email':per[0][7],'Personal Phone Number':per[0][6],'Username':per[0][8],'Personal Currency':per[0][9],'Personal Account Number':per[0][2],'Shop Name':shp[0][0],'Shop Address':shp[0][1],'Shop State/City':shp[0][2],'Shop Country':shp[0][3],'Shop Email':shp[0][5],'Shop Phone Number':shp[0][6],'Shop Account Number':shp[0][4],'Shop Type':shp[0][7],'Shop Picture':shp[0][10],'Shop Revenue':float(shp[0][11]),'Shop Expenditure':float(shp[0][12]),'Shop Currency':shp[0][13],'Number of Workers':shp[0][14],'Number of Products':shp[0][15],'Shop Roles':rol,'Shop Category':cat,'Shop Vacancy':vacdata}
    def edit_shop_data(self,data:dict,shopid):
        self.cur.execute('''SELECT ID FROM branch WHERE ID="%s"'''%shopid)
        a=sum(self.cur.fetchall(),())
        nsid=None
        if 'Name' in data:
            nsid=self.stop_collision_id(data['Name'][:3].upper()+shopid[3:],'Shop')        
        if len(a)==1:
            r=','.join(data)
            x=r.split(',')
            self.cur.execute('''SELECT %s FROM branch WHERE ID="%s"'''%(r,shopid))
            w=sum(self.cur.fetchall(),())
            for i in data:
                self.cur.execute('''UPDATE branch SET %s="%s" WHERE ID="%s"'''%(i,data[i],shopid))
            ans={}
            if nsid!=None:                
                self.cur.execute('''UPDATE branch SET ID="%s" WHERE ID="%s"'''%(nsid,shopid))
                self.cur.execute('''UPDATE employee SET Shop_ID="%s" WHERE Shop_ID="%s"'''%(nsid,shopid))
                self.cur.execute('''UPDATE employee_records SET Shop_ID="%s" WHERE Shop_ID="%s"'''%(nsid,shopid))
                self.cur.execute('''UPDATE owner SET Shop_ID="%s" WHERE Shop_ID="%s"'''%(nsid,shopid))
                self.cur.execute('''UPDATE product SET Supplier_Shop_ID="%s" WHERE Supplier_Shop_ID="%s"'''%(nsid,shopid))
                ans={'Shop ID':[shopid,nsid]}
            for i in range(len(x)):
                ans[x[i]]=[w[i],data[x[i]]]
            self.editshop=True
            self.type='Owner'
            self.track(ans,shopid)
            return 'Done'
        return 'Shop does not exists'
    def edit_user_data(self,data:dict,userid):
        self.cur.execute('''SELECT ID FROM owner WHERE ID="%s"'''%userid)
        a=sum(self.cur.fetchall(),())
        nuserid=None
        if 'Name' in data:
            n=data['Name'].split()
            n=n[0][0]+n[1][0]+n[2][0]
            nuserid=self.stop_collision_id(userid[:4]+n+userid[7:],'Personal')
        if len(a)==1:
            r=','.join(data)
            x=r.split(',')
            self.cur.execute('''SELECT %s FROM owner WHERE ID="%s"'''%(r,userid))
            w=sum(self.cur.fetchall(),())
            for i in data:
                self.cur.execute('''UPDATE owner SET %s="%s" WHERE ID="%s"'''%(i,data[i],userid))
            ans={}
            if nuserid!=None:
                self.cur.execute('''UPDATE owner SET ID="%s" WHERE ID="%s"'''%(nuserid,userid))
                self.cur.execute('''UPDATE branch SET Owner_ID="%s" WHERE Owner_ID="%s"'''%(nuserid,userid))
                self.cur.execute('''UPDATE user_password_ SET ID="%s" WHERE ID="%s"'''%(nuserid,userid))
                ans={'User ID':[userid,nuserid]}
            for i in range(len(x)):
                ans[x[i]]=[w[i],data[x[i]]]
            self.edituser=True
            self.type='Owner'
            self.track(ans,userid)
            return 'Done'
        else:
            self.cur.execute('''SELECT ID FROM employee WHERE ID="%s"'''%userid)
            a=sum(self.cur.fetchall(),())
            if len(a)==1:
                r=','.join(data)
                x=r.split(',')
                self.cur.execute('''SELECT %s FROM employee WHERE ID="%s"'''%(r,userid))
                w=sum(self.cur.fetchall(),())
                for i in data:
                    self.cur.execute('''UPDATE employee SET %s="%s" WHERE ID="%s"'''(i,data[i],userid))
                ans={}
                for i in range(x):
                    ans[x[i]]=[w[i],data[x[i]]]
                self.edituser=True
                self.type='Employee'
                self.track(ans,userid)
                return 'Done'
        return 'User does not exists'
    def get_vac_slots(self,rol,sid):
        s=0
        for i in rol:
            self.cur.execute('''SELECT Number_of_Slots FROM employ_records WHERE Role_ID="%s" AND Shop_ID="%s"'''%(i,sid))
            o=sum(self.cur.fetchall(),())
            if len(o)==1:
                s+=int(o[0])
        return s
    def get_recruit(self,rol,sid):
        d=[]
        for i in rol:
            self.cur.execute('''SELECT Vacancy_Code FROM employ_records WHERE Shop_ID="%s" AND Role_ID="%s" AND Number_of_Slots>0'''%(sid,i))
            o=sum(self.cur.fetchall(),())
            if len(o)==1:
                d.append(o[0])
        emp={}
        for i in d:
            self.cur.execute('''SELECT ID FROM recruit WHERE JSON_KEYS(Vacancy)="%s"'''%i)
            s=list(sum(self.cur.fetchall(),()))
            emp[i]=s
        return emp
    def return_rec(self,id):
        self.cur.execute('SELECT Name,Email,Phone_Number,Picture_URL,Gender,Home_Address,State_City,Country,DOB FROM recruit WHERE ID="%s"')
        return list(sum(self.cur.fetcall(),()))
    def close(self):
        self.con.close()