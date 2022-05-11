from cgitb import text
from kivy.app import App
from kivy.metrics import dp
from kivymd.font_definitions import theme_font_styles
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.properties import *
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.config import Config
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.datatables import MDDataTable
from kivycupertino.uix.textfield import CupertinoTextField
from kivycupertino.uix.control import *
import kivymd_extensions.akivymd as akivymd
from kivy_garden.xcamera import XCamera
from kivycupertino.app import CupertinoApp
from kivymd_akivymd_sylvia_dynamic.uix.card import MsCard
from kivymd.uix.refreshlayout import MDScrollViewRefreshLayout
from widget import NumText,FloatText,CatText,Nav,CountryList,DateGet,GenderSwitch,EmpTable,DateButton,LevList
import random,sys,datetime,shutil,socket,uuid,re,check,storesql,uuid,socket,encrypt

myaddr=':'.join(re.findall('..','%012x'%uuid.getnode()))+f' {socket.gethostbyname(socket.gethostname())} '+socket.gethostname()

class MyAppManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyAppManager,self).__init__(**kwargs)
        self.user_id=''
        self.store_id=''        
    def create_category(self,name:str,desc:str):
        n=name.text
        d=desc.text
        if check.createcat(n,d)=='All Checked':
            cid=encrypt.EnCrypt(self.user_id).get_cat_id(n,self.store_id)
            if myconnect.create_cat(cid,n,d,self.store_id,self.user_id,0)=='Done':
                MDDialog(text=f'Category: {n} with ID: {cid} has been created').open()
                name.text=''
                desc.text=''                
                self.ids.product.ids.addprod.disabled=False
                self.ids.product.ids.ediprod.disabled=False
                self.ids.product.ids.delprod.disabled=False
                self.ids.product.ids.ptab.default_tab=self.ids.product.ids.addcat.title
        else:
            MDDialog(text=check.createcat(name,desc)).open()
    def create_product(self):
        pname=self.ids.product.ids.pname.text.strip()
        uprice=self.ids.product.ids.uprice.text.strip()
        pmeasure=self.ids.product.ids.pmeasure.text.strip()
        pcat=self.ids.product.ids.pcat.text.strip()
        pdesc=self.ids.product.ids.pdesc.text.strip()
        supid=self.ids.product.ids.supid.text.strip()
        sushopid=self.ids.product.ids.supshid.text.strip()
        if pcat in self.ids.product.ids.pcat.words:
            cat=True
        else:
            cat=False        
        if uprice=='':
            self.ids.product.ids.uprice.text='0'
        if check.create_prod(pname,pmeasure,cat,pdesc,supid,sushopid) == 'All Checked':
            pid=encrypt.EnCrypt(self.user_id).get_prod_id(pname,self.store_id)
            catid=myconnect.get_cat('',self.store_id,pcat)[-1]
            rsupid=myconnect.getuser(supid,self.store_id)
            rsushpid=myconnect.getshop(sushopid,self.user_id)
            if len(rsupid)==len(rsushpid)==1:
                myconnect.create_prod(pid,pname,uprice,pmeasure,catid,pdesc,rsupid[0],rsushpid[0],self.store_id,self.user_id)
                self.ids.product.ids.pname.text=''
                self.ids.product.ids.uprice.text=''
                self.ids.product.ids.pmeasure.text=''
                self.ids.product.ids.pcat.text=''
                self.ids.product.ids.pdesc.text=''
                self.ids.product.ids.supid.text=''
                self.ids.product.ids.supshid.text=''                
                MDDialog(text=f'Product {pname} has been created').open()
            else:
                MDDialog(text='Enter Valid Supplier\'s Details').open()    
        else:
            MDDialog(text=str(check.create_prod(pname,pmeasure,pcat,pdesc,supid,sushopid))).open()
    def ask_prod(self,):
        box=MDBoxLayout(size_hint_y=None)
        self.w=CupertinoTextField(hint_text='Product ID / Name')
        c=MDFlatButton(text='CANCEL')
        s=MDRaisedButton(text='Submit')
        box.add_widget(self.w)
        self.pre=self.ids.product.ids.ptab.current
        self.a=MDDialog(title='Enter Product ID/Name',type='custom',content_cls=box,buttons=[c,s])
        c.on_release=self.leave_edit
        s.on_release=self.showeditprod
        self.a.open()
    def leave_edit(self):
        self.a.dismiss(force=False)
        self.ids.product.ids.ptab.switch_tab('ediprod')
        #self.ids.product.ids.ptab.switch_tab(self.ids.product.ids.ptab.previous_tab.name)    
    def eddis(self,mself,*wid):
        if mself.text=='Edit':
            for i in wid:
                i.disabled=False
            mself.text='Done'
        elif mself.text=='Done':
            for i in wid:
                i.disabled=True
            mself.text='Edit'
            nc=0
            for i in range(len(self.nn)):
                if i==1:
                    if float(self.l[i])!=float(self.nn[i].text):
                       nc+=1
                elif i==3:
                    self.nn[i].text=str(int(self.nn[i].text))
                    if int(self.l[i])>int(self.nn[i].text):
                        if len(self.ids.product.ids.epquantreason.text)>=6:
                            nc+=1
                            self.ids.product.ids.epquantreason.disabled=True
                        else:
                            self.ids.product.ids.epquantreason.text=''
                            Snackbar(text='Your Reasons must consist of 6 or more alphabetic characters').open()
                    else:
                        self.nn[i].text=str(int(self.l[i]))
                        self.ids.product.ids.epquantreason.size_hint_y=0
                        self.ids.product.ids.epquantreason.disabled=True
                elif i==4:
                    w=False
                    self.ids.product.ids.epcat.words=list(myconnect.get_cat(self.ids.product.ids.epcat.text,self.store_id))
                    for j in self.ids.product.ids.epcat.words:    
                        if j.startswith(self.ids.product.ids.epcat.text):
                            self.ids.product.ids.epcat.text=j
                            w=True
                            if self.ids.product.ids.epcat.text!=self.l[i]:
                                nc+=1
                            break
                    if w==False:
                        self.ids.product.ids.epcat.text=self.l[i]
                        Snackbar(text='Category does not exists').open()
                elif i==6:
                    if len(myconnect.getuser(self.nn[i].text,self.store_id))>0:
                        if self.nn[i].text!=self.l[i]:
                            nc+=1
                    else:
                        self.nn[i].text=self.l[i]
                        Snackbar(text='Supplier does not exists').open()
                elif i==7:
                    if len(myconnect.getshop(self.nn[i].text,self.user_id))>0:
                        if self.nn[i].text!=self.l[i]:
                            nc+=1
                    else:
                        self.nn[i].text=self.l[i]
                        Snackbar(text='Shop does not exists').open()
                else:                    
                    if i==0 or i==2:
                        u=4
                    else:
                        u=6
                    if self.nn[i].text!=self.l[i]:
                        if len(self.nn[i].text)>=u:
                            if self.nn[i].text.isalnum() and self.nn[i].text[0].isalpha():
                                self.nn[i].text=self.nn[i].text.title()
                                nc+=1                            
                            else:
                                if i==0:
                                    t='Product Name',4
                                elif i==2:
                                    t='Product Measure',4
                                elif i==5:
                                    t='Product Description',6
                                Snackbar(text=t[0]+' must consists of '+str(t[1])+' or more alphanumeric characters with the first as an alphabet.').open()
                                self.nn[i].text=self.l[i]
            if nc==1:
                self.ids.product.ids.editallprod.text='Apply Change (1)'
            elif nc>1:
                self.ids.product.ids.editallprod.text=f'Apply Changes ({nc})'
            else:
                self.ids.product.ids.editallprod.text=f'Apply Change(s)'
    def sqreas(self):
        self.ids.product.ids.editpquant.text='Done'      
        self.ids.product.ids.epquant.disabled=True
        if int(self.l[3])>int(self.nn[3].text):
            self.ids.product.ids.epquantreason.size_hint_y=.225
            self.ids.product.ids.epquantreason.disabled=False
        else:
            self.nn[3].text=str(int(self.l[3]))
            self.ids.product.ids.epquantreason.size_hint_y=0
            self.ids.product.ids.epquantreason.disabled=True
    def addlev(self,n):
        if n.isnumeric():
            if 0<int(n)<=20:
                self.ids.branch.ids.levbox.clear_widgets()
                self.ids.branch.ids.levbox.size_hint_y=0
                #self.ids.branch.ids.depbox.size_hint_y=1
                #self.ids.branch.ids.depcard.size_hint_y=.6
                for i in range(1,int(n)+1):            
                    self.ids.branch.ids.levbox.add_widget(MDLabel(text=f'Level {i}',size_hint=(.5,.1)))
                    self.ids.branch.ids.levbox.add_widget(CupertinoTextField(hint_text='Enter Name',size_hint=(.9,.2)))
                    self.ids.branch.ids.levbox.add_widget(CupertinoTextField(hint_text='Description',multiline=True,size_hint=(.9,.6)))
                    self.ids.branch.ids.levbox.add_widget(NumText(hint_text='Salary',size_hint=(.9,.35)))
                    #self.ids.branch.ids.depname.size_hint_y-=.035
                    #self.ids.branch.ids.depdesc.size_hint_y-=.035
                    #self.ids.branch.ids.nolevel.size_hint_y-=.035
                #if self.ids.branch.ids.depcard.size_hint_y<.9:
                #    self.ids.branch.ids.depcard.size_hint_y+=int(n)*.35
                #self.ids.branch.ids.depbox.size_hint_y+=int(n)*.1
                #self.ids.branch.ids.levbox.size_hint_y+=int(n)*1.8
            else:
                Snackbar(text='Number(s) of Level should be in range from 1 to 20').open()
        else:
                Snackbar(text='Enter Valid Number(s) of Level').open()
    def showeditprod(self):
        l=myconnect.get_prod(self.w.text,self.store_id)
        if l!=None:
            self.l=list(map(str,l))
            self.ids.product.ids.epquantreason.size_hint_y=0
            self.nn=self.ids.product.ids.epname,self.ids.product.ids.euprice,self.ids.product.ids.epmeasure,self.ids.product.ids.epquant,self.ids.product.ids.epcat,self.ids.product.ids.epdesc,self.ids.product.ids.esupid,self.ids.product.ids.esupshid
            self.a.dismiss()
            for ind,v in enumerate(self.nn):
                v.text=self.l[ind]
        else:
            Snackbar(text='Product does not exists').open()
    def editprod(self):
        self.editpbut=self.ids.product.ids.editpname,self.ids.product.ids.edituprice,self.ids.product.ids.editpmeasure,self.ids.product.ids.editpquant,self.ids.product.ids.editpcategory,self.ids.product.ids.editpdesc,self.ids.product.ids.editsupid,self.ids.product.ids.editsupshid
        self.editwid=[[self.ids.product.ids.epname],[self.ids.product.ids.euprice],[self.ids.product.ids.epmeasure],[self.ids.product.ids.epquant,self.ids.product.ids.epquantreason],[self.ids.product.ids.epcat],[self.ids.product.ids.epdesc],[self.ids.product.ids.esupid],[self.ids.product.ids.esupshid]]
        for i,v in enumerate(self.editpbut):
            if v.text=='Done':
                self.eddis(v,*self.editwid[i])
        e={}
        f={}
        r=''
        for i,v in enumerate(self.nn):
            if self.l[i]!=v.text:
                if i==0:
                    e['Name']=v.text
                    f['Name']=self.l[i]
                elif i==1:
                    e['Price']=float(v.text)
                    f['Price']=float(self.l[i])
                elif i==2:
                    e['Measure']=v.text
                    f['Measure']=self.l[i]
                elif i==3:                    
                    r=self.ids.product.ids.epquantreason.text
                    if r=='':
                        self.ids.product.ids.epquantreason.size_hint_y=0
                        self.ids.product.ids.epquant.text=self.l[3]
                    else:
                        e['Quantity']=int(v.text)
                        f['Quantity']=int(self.l[i])
                elif i==4:
                    e['CID']=v.text
                    f['CID']=self.l[i]
                elif i==5:
                    e['Desc']=v.text
                    f['Desc']=self.l[i]
                elif i==6:
                    e['SID']=v.text
                    f['SID']=self.l[i]
                elif i==7:
                    e['SHID']=v.text
                    f['SHID']=self.l[i]
        if e!={}:
            myconnect.edit_prod(self.l[-1],self.user_id,e,f,r)
            MDDialog(text='Changes has been applied').open()
    def del_prod(self):
        dpnamid=self.ids.product.ids.dpnameid.text
        reas=self.ids.product.ids.delreas.text
        if len(reas)>=6:
            delans=myconnect.del_prod(dpnamid,reas,self.store_id,self.user_id)
            if delans=='Deleted':
                MDDialog(text=f'Product {dpnamid} has been deleted').open()
            else:
                MDDialog(text=delans).open()
        else:
            Snackbar(text='Reasons must have 6 or more characters')
        pass
    def ask_emp(self):
        box=MDBoxLayout(size_hint_y=None)
        w=CupertinoTextField(hint_text='Employee ID / Name')
        c=MDFlatButton(text='CANCEL')
        s=MDRaisedButton(text='Submit')
        box.add_widget(w)
        self.pre=self.ids.product.ids.ptab.current
        self.a=MDDialog(title='Enter Employee ID/Name',type='custom',content_cls=box,buttons=[c,s])
        c.on_release=self.leave_edit
        s.on_release=self.showeditprod
        self.a.open()
        a=MDDialog()
    def create_slot(self):            
        depid=self.ids.employee.ids.ndepname.text.strip()
        lev=self.ids.employee.ids.level.text.strip()
        nslo=self.ids.employee.ids.slotnum.text.strip()
        start=self.ids.employee.ids.dateofstart
        end=self.ids.employee.ids.dateofend
        if nslo=='':
            self.ids.employee.ids.slotnum.text='0'
            nslo='0'    
        v=myconnect.get_dep(self.store_id,depid)
        if check.create_slot(lev,nslo,v,start,end)[0]=='All Checked':            
            myconnect.create_slot([check.create_slot(lev,nslo,v,start,end)[1],lev,nslo,self.store_id,self.user_id,start.s,end.s])
            MDDialog(text='Slots Created').open()
        else:                
            Snackbar(text=check.create_slot(lev,nslo,v,start,end)[0]).open()
    def get_dep_lev(self):
        pass
    def password_validate(self,useremail_wid,password_wid):
        password=password_wid.text
        useremail=useremail_wid.text
        if str(len(password)**0.5).split('.')[1]!='0':
            for i in range(int(len(password)**0.5),len(password)+1):
                if str(int(len(password)+i)**0.5).split('.')[1]=='0':
                    break
            password+='0'*i
        d=myconnect.search_user_email(useremail)
        if d==():
            Snackbar(text='Invalid Username/Email').open()
        else:
            w=False
            for i in d:
                s=encrypt.DeCrypt(i)
                if s.decipher()==password:                    
                    w=True
                    break
            if w==False:
                Snackbar(text='Incorrect Password').open()
            else:
                password_wid.text=''
                useremail_wid.text=''
                ww=encrypt.EnCrypt(password).password()
                self.user_id=myconnect.get_userid(useremail,ww)[-1]
                self.store_id=myconnect.get_shop_id_from_userid(self.user_id)
                myconnect.savelogin=True
                myconnect.type='Owner'
                myconnect.track(self.user_id,self.store_id)
                self.current='home'
    def change_pass(self):
        self.fue=self.ids.forgotpass.ids.forgotuseremail.text
        st=False
        for n in myconnect.get_user_email():
            if self.fue in n:
                st=True
                break
        if st:
            alnum=[chr(i) for i in range(65,91)]
            alnum.extend([chr(i) for i in range(48,58)])
            al=''
            for i in range(6):
                al+=random.choice(alnum)
            myconnect.ins_change_user_pass(self.fue,al)
            self.current='changepass'
            #######EMAIL SENT#########
    def update_pass(self,access,newpass,connewpass):
        accesstext=access.text.strip()
        newpasstext=newpass.text.strip()
        conpasstext=connewpass.text.strip()
        usemail=self.ids.forgotpass.ids.forgotuseremail.text.strip()
        if len(newpasstext)<8 or newpasstext.isalnum()==False:
            g=False
        else:
            g=True
        if newpasstext==conpasstext and g:
            passw=encrypt.EnCrypt(newpasstext)
            MDDialog(text=str(myconnect.change_pass(accesstext,passw.password(),usemail))).open()
            self.current='login'
            access.text=''
            newpass.text=''
            connewpass.text=''
            self.ids.forgotpass.ids.forgotuseremail.text=''
        else:
            if g==False:
                t='Password should be 8 or more alphanumeric characters'
            else:
                t='Password has not been confirmed.'
            Snackbar(text=t).open()
    def ask_lev(self):
        box=MDBoxLayout(size_hint_y=None,orientation='vertical',height=dp(200),spacing=10)
        w=CupertinoTextField(hint_text='Name',size_hint_y=.2)
        x=CupertinoTextField(hint_text='Description',multiline=True,size_hint_y=.35)
        f.a.y=NumText(hint_text='Salary',size_hint_y=.22)
        c=MDFlatButton(text='CANCEL')
        s=MDRaisedButton(text='Submit')
        box.add_widget(w)
        box.add_widget(x)
        box.add_widget(y)
        self.a=MDDialog(title='Level',type='custom',content_cls=box,buttons=[c,s],radius=[20,5,20,5])
        #c.on_release=self.leave_edit
        #s.on_release=self.showeditprod
        self.a.open()
    def save_lev(self,name,desc,sal):
        if check.create_lev(name,desc)=='All Checked':
            self.ids.employee.levbox.size_hint_y+=.2
            self.ids.employee.levbox..add_widget(LevList(text=name))
        else:
            Snackbar(text=check.create_lev(name,desc)).open()
    def change_screen(self,name:str):
        if name=='create':
            self.fname=self.ids.new.ids.fname.text.strip()
            self.lname=self.ids.new.ids.lname.text.strip()
            self.oname=self.ids.new.ids.oname.text.strip()
            self.username=self.fname.lower()+self.lname.lower()
            if self.ids.new.ids.male.state == 'down':
                self.gender='Male'
            elif self.ids.new.ids.female.state == 'down':
                self.gender='Female'
            else:
                self.gender=''                
            self.password=self.ids.new.ids.password.text.strip()
            self.address=self.ids.new.ids.address.text.strip()
            self.email=self.ids.new.ids.email.text.strip()
            self.pnum=self.ids.new.ids.pnum.text.strip()
            self.ccode=self.ids.new.ids.ccode.text.strip()
            self.dob=self.ids.new.ids.dob.text.strip()
            for ind,val in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']):
                if self.dob.split()[1].title()==val:
                    m=ind+1
                    break
            if check.new(self.fname,self.lname,self.oname,self.dob,self.password,self.address,self.email,self.ccode,self.pnum,self.gender)=='All Checked':
                self.ddob=datetime.date(int(self.dob.split()[3]),m,int(self.dob.split()[2]))                
                self.current=name
            else:
                a=MDDialog()
                a.text=check.new(self.fname,self.lname,self.oname,self.dob,self.password,self.address,self.email,self.ccode,self.pnum,self.gender)
                a.open()
        elif name=='join':
            sid=self.ids.join.ids.joinsid.text
        elif name=='home':
            self.sname=self.ids.create.ids.sname.text.strip()
            self.saddr=self.ids.create.ids.saddr.text.strip()
            self.semail=self.ids.create.ids.semail.text.strip()
            self.scode=self.ids.create.ids.scode.text.strip()
            self.spnum=self.ids.create.ids.spnum.text.strip()
            if check.create_shop(self.sname,self.saddr,self.semail,self.scode,self.spnum)=='All Checked':                
                a=encrypt.EnCrypt(self.sname)
                self.sid=a.shop_id()
                self.pid=a.person_id(f'{self.fname} {self.lname} {self.oname}')
                passw=encrypt.EnCrypt(self.password)
                person=[self.pid,f'{self.fname} {self.lname} {self.oname}',self.gender,self.ddob,self.sid,'newaccount.png','None',100.0,self.address,f'{self.ccode}-{self.pnum}',self.email,self.username,passw.password(),True,myaddr]
                shop=[self.sid,self.sname,self.saddr,self.pid,'None',self.semail,f'{self.scode}-{self.spnum}','HQ','newshop.png',0.0,0.0,0,0]
                myconnect.create_person_shop(person,shop)
                self.current=name
                self.user_id=self.pid
                self.store_id=self.sid
            else:
                a=MDDialog()
                a.text=check.create_shop(self.sname,self.saddr,self.semail,self.scode,self.spnum)
                a.open()
        elif name in ['product','employee','branch']:
            self.ids.home_drawer.set_state('dismiss')            
            self.ids.home_manager.current=name
            self.ids.product.ids.pcat.words=list(myconnect.get_cat(self.ids.product.ids.pcat.text,self.store_id))
            if name=='product':
                if len(myconnect.get_sid_cat(self.store_id))<1:
                    self.ids.product.ids.addprod.disabled=True
                    self.ids.product.ids.ediprod.disabled=True
                    self.ids.product.ids.delprod.disabled=True
                else:
                    self.ids.product.ids.addprod.disabled=False
                    self.ids.product.ids.ediprod.disabled=False
                    self.ids.product.ids.delprod.disabled=False
        elif name=='homenologin':
            self.ids.home_manager.current='home'
        else:
            self.current=name
    def create_dep(self):
        depn=self.ids.branch.ids.depname.text
        depdesc=self.ids.branch.ids.depdesc.text
        nolevel=self.ids.branch.ids.nolevel.text
        if check.create_dep(depn,depdesc)=='All Checked':
            did=encrypt.EnCrypt(depn).dep_id(depn,self.store_id)
            myconnect.create_dep([did,depn,self.store_id,depdesc,nolevel,self.user_id])
        else:
            MDDialog(text=check.create_dep(depn,depdesc)).open()
    def enter_home(self,name):    
        self.ids.home.ids.welcome.text='Welcome '+name
        
class SplashScreen(MDScreen):
    def __init__(self, **kwargs):
        super(SplashScreen,self).__init__(**kwargs)            
class New(MDScreen):
    def __init__(self, **kwargs):
        super(New,self).__init__(**kwargs)
class Create(MDScreen):
    def __init__(self, **kwargs):
        super(Create,self).__init__(**kwargs)
class Join(MDScreen):
    def __init__(self, **kwargs):
        super(Join,self).__init__(**kwargs)
class Login(MDScreen):
    def __init__(self, **kwargs):
        super(Login,self).__init__(**kwargs)
class Home(MDScreen):
    def __init__(self, **kwargs):
        super(Home,self).__init__(**kwargs)

class MyStoreApp(MDApp,CupertinoApp):
    def __init__(self, **kwargs):
        super(MyStoreApp,self).__init__(**kwargs)            
        self.newshop='newshop.png'
        self.newaccount='newaccount.png'
        self.theme_cls.font_styles['Cascadia Code']=['Cascadia Code',16,False,0.2]   
        self.country=[
            {
                'text':f'+{check.country[i][2]} {check.country[i][1]}',
                'viewclass':'CountryList',
                'icon':f'country/{i.lower()}.png',
                'on_release':lambda x=[f'+{check.country[i][2]} {check.country[i][1]}',f'country/{i.lower()}.png']:self.change_count_name(self.root.ids.new.ids.ccode,x[0],self.countrydrop,x[1])
            } for i in check.country
        ]
        self.scount=[
            {
                'text':f'+{check.country[i][2]} {check.country[i][1]}',
                'viewclass':'CountryList',
                'icon':f'country/{i.lower()}.png',
                'on_release':lambda x=[f'+{check.country[i][2]} {check.country[i][1]}',f'country/{i.lower()}.png']:self.change_count_name(self.root.ids.create.ids.scode,x[0],self.sdrop,x[1])
            } for i in check.country
        ]        
    def ch(self,s):
        if s=='cam':
            self.cam=XCamera()
            self.root.current='acamera'
            self.root.ids.acamera.add_widget(self.cam)
            self.cam.allow_stretch=True
            #self.cam.shoot()
            #self.root.ids.acamera.ids.ac_camera.disabled=False
            #self.root.ids.acamera.ids.ac_camera.allow_stretch=True
            #self.root.ids.acamera.ids.ac_camera.play=False
        elif s=='fold':
            ()  
    def acc_pic_open(self):
        self.pic_bottom=MDGridBottomSheet()
        self.pic_bottom.add_item("Camera",lambda _:self.ch('cam'),icon_src='camera')
        self.pic_bottom.add_item("File",lambda _:self.ch('fold'),icon_src='folder')
        self.pic_bottom.open()
    def validate_num(self,wid):
        if wid.text.isalpha()==False:
            MDDialog(text='Fake').open()
    def build(self):
        Window.size=350,600
        self.countrydrop=MDDropdownMenu(position='auto',caller=self.root.ids.new.ids.ccode,items=self.country,width_mult=4,size_hint_y=.4)
        self.sdrop=MDDropdownMenu(position='auto',caller=self.root.ids.create.ids.scode,items=self.scount,width_mult=4)
        self.emptable=MDDataTable(use_pagination=True,check=True,column_data=[('ID',dp(30)),('Department',dp(40)),('Level',dp(40))])
        #self.root.ids.employee.ids.empcard.add_widget(self.emptable)
        self.now=datetime.datetime.now()
        self.datepick=DateGet()
        self.datepick.on_save=lambda x,y:self.change_dob(self.root.ids.new.ids.dob,datetime.date(self.datepick.sel_year,self.datepick.sel_month,self.datepick.sel_day).ctime().replace('00:00:00',''))
        self.datepick.max_date=datetime.date(2000,1,20)
        Config.set('input', 'mouse', 'mouse,disable_multitouch')
        Config.write()
    def on_start(self):
        self.splash=self.root.ids.splash
        #self.theme_cls=0,1,.5
        self.ip=f' {socket.gethostbyname(socket.gethostname())} '
        self.mac=':'.join(re.findall('..','%012x'%uuid.getnode()))
        self.host=socket.gethostname()
        if myconnect.get_device(self.mac) or myconnect.get_device(self.ip) or myconnect.get_device(self.host):
            s='login'
        else:
            s='new'
        self.sptime=Clock.schedule_once(lambda _:self.root.change_screen(s),1)
        #self.root.current='create'
    def change_dob(self,obj,name):
        obj.text=name
        self.datepick.dismiss()
    def change_count_name(self,obj,name,subj,icon):
        obj.text=name
        obj.source=icon
        subj.dismiss()
if __name__=='__main__':
    app=MyStoreApp()
    app.title='MyStore'
    myconnect=storesql.Connect()
    app.theme_cls.primary_palette='LightGreen'
    app.theme_cls.accent_palette='Green'
    app.theme_cls.primary_hue='600'
    LabelBase.register('Cascadia Code',fn_bold='CascadiaCode.ttf',fn_regular='CascadiaCode.ttf')
    theme_font_styles.append('Cascadia Code')
    app.run()
