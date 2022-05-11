def new(fname,lname,oname,dob,password,address,email,ccode,pnum,gender):
    if not fname.istitle():
        return 'First Name should start with uppercase'
    if not fname.isalpha():
        return 'First Name should only contain alphabetic characters'
    if not lname.istitle():
        return 'Last Name should start with uppercase'
    if not lname.isalpha():
        return 'Last Name should only contain alphabetic characters'
    if not oname.istitle():
        return 'Other Name should start with uppercase'
    if not oname.isalpha():
        return 'Other Name should only contain alphabetic characters'
    if gender not in ['Male','Female']:
        return 'No Gender Selected'
    if len(password)<8:
        return 'Password must be 8 or more characters long'
    if password.isalnum()==False:
        return 'Password must contain only alphanumeric characters'     
    if len(address)<15:
        return 'Home Address is too short'
    if dob.title() == 'Select Date Of Birth':
        return 'Date of Birth has not been selected'
    if len(email)<5:
        return 'Invalid Email Address entered'
    if not(email[0].isalpha()):
        return 'Email Address should start with alphabetic characters'
    e=False
    for i in ['gmail.com','yahoo.com','hotmail.com','aol.com','hotmail.co.uk','hotmail.fr','msn.com','yahoo.fr','wandoo.fr','orange.fr','comcast.net','yahoo.co.uk','yahoo.com.br','yahoo.co.in','live.com','rediffmail.com','free.fr','gmx.de','web.de','yandex.ru','ymail.com','libero.it','outlook.com','uol.com.br','bol.com.br','mail.ru','cox.net','hotmail.it','sbcglobal.net','sfr.fr','live.fr','verizon.net','live.co.uk','googlemail.com','yahoo.es','ig.com.br','live.nl','bigpond.com','terra.com.br','yahoo.it','neuf.fr','yahoo.de','alice.it','rocketmail.com','att.et','laposte.net','facebook.com','bellsouth.net','yahoo.in','hotmail.es','charter.net','yahoo.ca','yahoo.com.au','rambler.ru','hotmail.de','tiscali.it','shaw.ca','yahoo.co.jp','sky.com','earthlink.net','optonline.net','freenet.de','t-online.de','aliceadsl.fr','virgilio.it','home.nl','qq.com','telnet.be','me.com','yahoo.com.ar','tiscali.co.uk','yyahoo.com.mx','voila.fr','gmx.net','mail.com','planet.nl','tin.it','live.it','ntlworld.com','arcor.de','yahoo.co.id','frontiernet.net','hetnet.nl','live.com.au','yahoo.com.sg','zonnet.nl','club-internet.fr','juno.com','optusnet.com.au','blueyonder.co.uk','bluewin.ch','skynet.be','sympatico.ca','windstream.net','mac.com','centurytel.net','chello.nl','live.ca','aim.com','bigpond.net.au']:
        if email.endswith(i):
            e=True
            break
    if not e:
        return 'Wrong email domain name'    
    if ccode.title() == 'Country Code':
        return 'Country Code not selected'
    if pnum.isdigit()==False:
        return 'Invalid Phone Number entered'    
    if not 10<=len(pnum)<=15:        
        return 'Phone Number must be between 10 to 15 digits'
    return 'All Checked'
def create_shop(sname,saddr,semail,scode,spnum):
    if not sname.isalnum():
        return 'Shop Name should only contain alphanumeric characters'
    if len(sname)<3:
        return 'Shop Name should contain 3 or more alphanumeric character'
    if not sname[0].isupper() :
        return 'Shop Name must begin with uppercase'
    if len(saddr)<15:
        return 'Shop Address is too short'
    if len(semail)<10:
        return 'Invalid Email Address entered'
    e=False
    for i in ['gmail.com','yahoo.com','hotmail.com','aol.com','hotmail.co.uk','hotmail.fr','msn.com','yahoo.fr','wandoo.fr','orange.fr','comcast.net','yahoo.co.uk','yahoo.com.br','yahoo.co.in','live.com','rediffmail.com','free.fr','gmx.de','web.de','yandex.ru','ymail.com','libero.it','outlook.com','uol.com.br','bol.com.br','mail.ru','cox.net','hotmail.it','sbcglobal.net','sfr.fr','live.fr','verizon.net','live.co.uk','googlemail.com','yahoo.es','ig.com.br','live.nl','bigpond.com','terra.com.br','yahoo.it','neuf.fr','yahoo.de','alice.it','rocketmail.com','att.et','laposte.net','facebook.com','bellsouth.net','yahoo.in','hotmail.es','charter.net','yahoo.ca','yahoo.com.au','rambler.ru','hotmail.de','tiscali.it','shaw.ca','yahoo.co.jp','sky.com','earthlink.net','optonline.net','freenet.de','t-online.de','aliceadsl.fr','virgilio.it','home.nl','qq.com','telnet.be','me.com','yahoo.com.ar','tiscali.co.uk','yyahoo.com.mx','voila.fr','gmx.net','mail.com','planet.nl','tin.it','live.it','ntlworld.com','arcor.de','yahoo.co.id','frontiernet.net','hetnet.nl','live.com.au','yahoo.com.sg','zonnet.nl','club-internet.fr','juno.com','optusnet.com.au','blueyonder.co.uk','bluewin.ch','skynet.be','sympatico.ca','windstream.net','mac.com','centurytel.net','chello.nl','live.ca','aim.com','bigpond.net.au']:
        if semail.endswith(i):
            e=True
            break
    if not e:
        return 'Wrong email domain name'
    if not(semail[0].isalpha()):
        return 'Email Address should start with alphabetic characters'
    if scode.title() == 'Country Code':
        return 'Country Code not selected'
    if spnum.isdigit()==False:
        return 'Invalid Phone Number entered'    
    if not 10<=len(spnum)<=15 and spnum.isdigit()==False:
        return 'Invalid Phone Number entered'
    return 'All Checked'
def createcat(name,desc):
    if not name.isalnum():
        return 'Category Name should only contain alphanumeric characters'
    if len(name)<3:
        return 'Category Name should contain 3 or more alphanumeric character'
    if not name[0].isupper() :
        return 'Category Name must begin with uppercase'
    if len(desc)<15 or len(desc)>140:
        return 'Category Description must be between the range of 15 to 40 characters'
    return 'All Checked'
def create_prod(name,measure,cat,desc,supiduser,supshopiduser):
    if len(name)<4 and not name.isalpha():
        return 'Product Name must have 4 or more alphabetic characters'
    if not measure.isalpha() and len(measure)<4:
        return 'Measure must have 4 or more alphabetic characters only'
    if not cat:
        return 'Product Category does not exists'
    if len(desc)<6 and not desc.isalnum():
        return 'Description must have 6 or more alphanumeric characters only'
    if not desc[0].isalpha():
        return 'Description must start with alphabetic characters'
    if len(supiduser.strip())<6 and not supiduser.isalnum():
        return 'Supplier\'s ID/Username must have 6 or more non-space alphanumeric characters'
    if len(supshopiduser.strip())<6 and not supshopiduser.isalnum():
        return 'Supplier\'s Shop ID/Name must have 6 or more non-space alphanumeric characters'
    return 'All Checked'
def create_dep(name,desc):
    if len(name)<4:
        return 'Department Name must have 4 or more alphanumeric characeters only'
    if not name[0].isupper():
        return 'Department Name must start with an uppercase alphabet'
    if len(desc)<6:
        return 'Description must have 6 or more alphanumeric characters only'   
    if not desc[0].isalpha():
        return 'Description must start with alphabetic characters'
    return 'All Checked'
def create_slot(lev,nslo,v,start,end):
    idd=''
    if v==[]:
        return 'Department does not exists',idd
    if not lev.isnumeric():
        return 'Invalid Department Level',idd
    for i in v:
        if int(lev)!=0 and int(lev)<=int(i[1]):
            c=False
            idd=i[0]
            break
        else:
            c=True
    if c:
        return 'Department Level does not exists',idd
    if int(nslo)<1:
        return 'Invalid Number of Slots',idd
    if start.text=='Start Date':
        return 'Start Date not Selected',idd
    if end.text=='End Date':
        return 'End Date not Selected',idd
    return 'All Checked',idd
def create_lev(name,desc):
    if not name.isalnum():
        return 'Level Name must be alphanumeric characters'
    if len(name)<4:
        return 'Level Name must be 4 or more alphanumeric characters'
    if not name[0].isupper():
        return 'Level Name must start with an uppercase charcter'
    if not desc[0].isupper():
        return 'Description must start with an uppercase charcter'
    if len(desc)<8:
        return 'Description must be 8 or more alphanumeric characters'
    return 'All Checked'
country={'AD':['Andorra','AND','376','EUR','European Euro'],
    'AE':['United Arab Emirates','ARE','971','AED','UAE Dirham'],
    'AF':['Afghanistan','AFG','93','AFN','Afghan Afghani'],
    'AG':['Antigua and Barbuda','ATG','1268','XCD','East Carribean Dollar'],
    'AI':['Anguilla','AIA','1264','XCD','East Carribean Dollar'],
    'AL':['Albania','ALB','355','ALL','Albenian Lek'],
    'AM':['Armenia','ARM','374','AMD','Armenian Dram'],
    'AO':['Angola','AGO','244','AOA','Angola Kwanza'],
    'AQ':['Antarctica','ATA','672','AAD','Antarctican Dollar'],
    'AR':['Argentina','ARG','54','ARS','Argentine Peso'],
    'AS':['American Samoa','ASM','1684','USD','United States Dollar'],
    'AT':['Austria','AUT','43','EUR','European Euro'],
    'AU':['Australia','AUS','61','AUD','Australian Dollar'],
    'AW':['Aruba','ABW','297','AWG','Aruba Florin'],
    'AX':['Aland Islands','ALA','35818','EUR','European Euro'],
    'AZ':['Azerbaijan','AZE','994','AZN','Azerbaijan Manat'],
    'BA':['Bosnia and Herzegovina','BIH','387','BAM','Bosnia and Herzegovina Convertible Mark'],
    'BB':['Barbados','BRB','1246','BBD','Barbadian Dollar'],
    'BD':['Bangladesh','BGD','880','BDT','Bangladeshi Taka'],
    'BE':['Belgium','BEL','32','EUR','European Euro'],
    'BF':['Burkina Faso','BFA','226','XOF','West African CFA Franc'],
    'BG':['Bulgaria','BGR','359','BGN','Bulgarian Lev'],
    'BH':['Bahrain','BHR','973','BHD','Bahraini Dinar'],
    'BI':['Burundi','BDI','257','BIF','Burundi Franc'],
    'BJ':['Benin','BEN','229','XOF','West African CFA Franc'],
    'BL':['Saint Barthelemy','BLM','590','EUR','European Euro'],
    'BM':['Bermuda','BMU','1441','BMD','Bermudian Dollar'],
    'BN':['Brunei','BRN','673','BND','Brunei Dollar'],
    'BO':['Bolivia','BOL','591','BOB','Bolivian Boliviano'],
    'BQ':['Bonaire,Sint Eustatius and Saba','BES','599','USD','United States Dollar'],
    'BR':['Brazil','BRA','55','BRL','Brazillan Real'],
    'BS':['Bahamas','BHS','1242','BSD','Bahamian Dollar'],
    'BT':['Bhutan','BTN','975','BTN','Bhutanese Ngultrum'],
    'BV':['Bouvet Island','BVT','47','NOK','Norwegian Krone'],  
    'BW':['Botswana','BWA','267','BWP','Botswana Pula'],
    'BY':['Belarus','BLR','375','BYN','Belarusian Rubie'],
    'BZ':['Belize','BLZ','501','BZD','Belize Dollar'],
    'CA':['Canada','CAN','1','CAD','Canadian Dollar'],
    'CC':['Cocos (Keeling) Islands','CCK','61','AUD','Australian Dollar'],
    'CD':['Democratic Republic of the Congo','COD','243','CDF','Conglese Franc'],
    'CF':['Central African Republic','CAF','236','XAF','Central African CFA Franc'],
    'CG':['Congo','COG','242','XAF','Central African CFA Franc'],
    'CH':['Switzerland','CHE','41','CHF','Swiss Franc'],
    'CI':["Ivory Coast (Côte d'Ivoire)",'CIV','225','XOF','West African CFA Franc'],
    'CK':['Cook Islands','COK','682','CKD','Cook Islands Dollar'],
    'CL':['Chile','CHL','56','CLP','Chilean Peso'],
    'CM':['Cameroon','CMR','237','XAF','Central Afrian CFA Franc'],
    'CN':['China','CHN','86','CNY','Chinese Yuan Renminbi'],
    'CO':['Colombia','COL','57','COP','Colombian Peso'],
    'CR':['Costa Rica','CRC','506','CRC','Costa Rican Colon'],
    'CU':['Cuba','CUB','53','CUP','Cuban Peso'],
    'CV':['Cape Verde','CPV','238','CVE','Capo Verdean Peso'],
    'CW':['Curacao','CUW','599','ANG','Netherlands Antillean Guilder'],
    'CX':['Christmas Island','CXR','61','AUD','Australian Dollar'],
    'CY':['Cyprus','CYP','357','EUR','European Euro'],
    'CZ':['Czech Republic','CZE','420','CZK','Czech Koruna'],
    'DE':['Germany','DEU','49','EUR','European Euro'],
    'DJ':['Djibouti','DJI','253','DJF','Djiboutian Franc'],
    'DK':['Denmark','DNK','45','DKK','Danish Krone'],
    'DM':['Dominica','DMA','1767','XCD','East Carribean Dollar'],
    'DO':['Dominican Republic','DOM','1809','DOP','Dominican Peso'],
    'DZ':['Algeria','DZA','213','DZD','Algerian Dinar'],
    'EC':['Ecuador','ECU','593','USD','United States Dollar'],
    'EE':['Estonia','EST','372','EUR','European Euro'],
    'EG':['Egypt','EGY','20','EGP','Egyptian Pound'],
    'EH':['Western Sahara','ESH','212','EHP','Sahrawi Peseta'],
    'ER':['Eritrea','ERI','291','ERN','Eritrean Nakfa'],
    'ES':['Spain','ESP','34','EUR','European Euro'],
    'ET':['Ethiopia','ETH','251','ETB','Ethopian Birr'],
    'FI':['Finland','FIN','358','EUR','European Euro'],
    'FJ':['Fiji','FJI','679','FJD','Fijian Dollar'],
    'FK':['Falkland Islands','FLK','500','FKP','Falkland Islands Pound'],
    'FM':['Micronesia','FSM','691','USD','United States Dollar'],
    'FO':['Faroe Islands','FRO','298','FOK','Faroese Krona'],
    'FR':['France','FRA','33','EUR','European Euro'],
    'GA':['Gabon','GAB','241','XAF','Central African CFA Franc'],
    'GB':['United Kingdom','GBR','44','GBP','Pound Sterling'],
    'GB-ENG':['England','GBR-ENG','44','GBP','Pound Sterling'],
    'GB-NIR':['North Ireland','GBR-NIR','44','GBP','Pound Sterling'],
    'GB-SCT':['Scotland','GBR-SCT','44','GBP','Pound Sterling'],
    'GB-WLS':['Wales','GBR-WLS','44','GBP','Pound Sterling'],
    'GD':['Grenada','GRD','1473','XCD','East Carribean Dollar'],
    'GE':['Georgia','GEO','995','GEL','Georgian Lari'],
    'GF':['French Guiana','GUF','594','EUR','European Euro'],
    'GG':['Bailiwick of Guernsey','GGY','44','GGP','Guernsey Pound'],
    'GH':['Ghana','GHA','233','GHS','Ghanaian Pound'],
    'GI':['Gibraltar','GIB','350','GIP','Gibraltar Pound'],
    'GL':['Greenland','GRL','299','DKK','Danish Krone'],
    'GM':['Gambia','GMB','220','GMD','Gambian Dalasi'],
    'GN':['Guinea','GIN','224','GNF','Guinean Franc'],
    'GP':['Guadeloupe','GLP','590','EUR','European Euro'],
    'GQ':['Equatorial Guinea','GNQ','240','XAF','Central African CFA Franc'],
    'GR':['Greece','GRC','30','EUR','European Euro'],
    'GS':['South Georgia and South Sandwich Islands','SGS','500','GBP','Pound Sterling'],
    'GT':['Guatemala','GTM','502','GTQ','Guaternalan Quetzal'],
    'GU':['Guam','GUM','1671','USD','GTQ','United States Dollar'],
    'GW':['Guinea-Bissau','GNB','245','XOF','West African CFA Franc'],
    'GY':['Guyana','GUY','592','GYD','Guyanese Dollar'],
    'HK':['Hong Kong','HKG','852','HKD','Hong Kong Dollar'],
    'HM':['Heard Island and McDonald Islands','HMD','672','AUD','Australian Dollar'],
    'HN':['Honduras','HND','504','HKD','Honduran Lempira'],
    'HR':['Croatia','HRV','385','HRK','Croatian Kuna'],
    'HT':['Haiti','HTI','509','HTG','Haitian Gourde'],
    'HU':['Hungary','HUN','36','HUF','Hungarian Forint'],
    'ID':['Indonesia','IDN','62','IDR','Indonesian Rupiah'],
    'IE':['Ireland','IRL','353','EUR','European Euro'],
    'IL':['Israel','ISR','972','ILS','Israeli New Shekel'],
    'IM':['Isle of Man','IMN','44','IMP','Manx Pound'],
    'IN':['India','IND','91','INR','Indian Ruppe'],
    'IO':['British Indian Ocean Territory','IOT','246','USD','United States Dollar'],
    'IQ':['Iraq','IRQ','964','IQD','Iraqi Dinar'],
    'IR':['Iran','IRN','98','IRR','Iranian Rial'],
    'IS':['Iceland','IS','354','ISK','Icelandic Krona'],
    'IT':['Italy','ITA','39','EUR','European Euro'],
    'JE':['Jersey','JEY','44','JEP','Jersey Pound'],
    'JM':['Jamaica','JAM','1876','JMD','Jamaican Dollar'],
    'JO':['Jordan','JOR','962','JOD','Jordanian Dollar'],
    'JP':['Japan','JPN','81','JPY','Japanese Yuan'],
    'KE':['Kenya','KEN','254','KES','Kenyan Shilling'],
    'KG':['Kyrgyzstan','KGZ','996','KGS','Kyrgyzstani Som'],
    'KH':['Cambodia','KHM','855','KHR','Cambodian Riel'],
    'KI':['Kiribati','KIR','686','AUD','Australian Dollar'],
    'KM':['Comoros','COM','269','KMF','Comorian Franc'],
    'KN':['Saint Kitts and Nevis','KNA','1869','XCD','East Caribbean Dollar'],
    'KP':['North Korea','PRK','850','KPW','North Korean Won'],
    'KR':['South Korea','KOR','82','KRW','South Korean Won'],
    'KW':['Kuwait','KWT','965','KWD','Kuwaiti Dinar'],
    'KY':['Cayman Islands','CYM','1345','KYD','Cayman Islands Dollar'],
    'KZ':['Kazakhstan','KAZ','7','KZT','Kazakhstani Tenge'],
    'LA':['Laos','LAO','856','LAK','Laos Kip'],
    'LB':['Lebanon','LBN','961','LBP','Lebanese Pound'],
    'LC':['Saint Lucia','LCA','1758','XCD','East Caribbean Dollar'],
    'LI':['Liechtenstein','LIE','423','CHF','Swiss Franc'],
    'LK':['Sri Lanka','LKA','94','LKR','Sri Lanka Rupee'],
    'LR':['Liberia','LBR','231','LRD','Liberian Dollar'],
    'LS':['Lesotho','LSO','266','LSL','Lesotho Loti'],
    'LT':['Lithuania','LTU','370','EUR','European Euro'],
    'LU':['Luxembourg','LUX','352','EUR','European Euro'],
    'LV':['Latvia','LVA','371','EUR','European Euro'],
    'LY':['Libya','LBY','218','LYD','Libyan Dinar'],
    'MA':['Morocco','MAR','212','MAD','Moroccan Dirham'],
    'MC':['Monaco','MCO','377','EUR','European Euro'],
    'MD':['Moldova','MDA','373','MDL','Moldovan Leu'],
    'ME':['Montenegro','MNE','382','EUR','European Euro'],
    'MF':['Saint Martin','MAF','590','EUR','European Euro'],
    'MG':['Madagascar','MDG','261','MGA','Madagascar Ariary'],
    'MH':['Marshall Islands','MHL','692','USD','United States Dollar'],
    'MK':['Macedonia','MKD','389','MKD','Macedonian Denar'],
    'ML':['Mali','MLI','223','XOF','West African CFA Franc'],
    'MM':['Myanmar (Burma)','MMR','95','MMK','Myanmar Kyat'],
    'MN':['Mongolia','MNG','976','MNT','Mongolian Tugrik'],
    'MO':['Macau','MAC','853','MOP','Macanese Pataca'],
    'MP':['Northern Mariana Islands','MNP','1670','USD','United States Dollar'],
    'MQ':['Martinique','MTQ','596','EUR','European Euro'],
    'MR':['Mauritania','MRT','222','MRU','Mauritanian Ouguiya'],
    'MS':['Montserrat','MSR','1664','XCD','East Caribbean Dollar'],
    'MT':['Malta','MLT','356','EUR','European Euro'],
    'MU':['Mauritius','MUS','230','MUR','Mauritian Rupee'],
    'MV':['Maldives','MDV','960','MVR','Maldivian Rufiyaa'],
    'MW':['Malawi','MWI','265','MWK','Malawian Kwacha'],
    'MX':['Mexico','MEX','52','MXN','Mexican Peso'],
    'MY':['Malaysia','MYS','60','MYR','Malaysian Ringgit'],
    'MZ':['Mozambique','MOZ','258','MZN','Mozambican Metical'],
    'NA':['Namibia','NAM','264','NAD','Namibian Dollar'],
    'NC':['New Caledonia','NCL','687','XPF','CFP Franc'],
    'NE':['Niger','NER','227','XOF','West African CFA Franc'],
    'NF':['Norfolk Island','NFK','672','AUD','Australian Dollar'],
    'NG':['Nigeria','NGA','234','NGN','Nigerian Naria'],
    'NI':['Nicaragua','NIC','505','NIO','Nicaraguan Cordoba'],
    'NL':['Netherlands','NLD','31','EUR','European Euro'],
    'NO':['Norway','NOR','47','NOK','Norwegian Krone'],
    'NP':['Nepal','NPL','977','NPR','Nepalese Rupee'],
    'NR':['Nauru','NRU','674','AUD','Australian Dollar'],
    'NU':['Niue','NIU','683','NZD','New Zealand Dollar'],
    'NZ':['New Zealand','NZL','64','NZD','New Zealand Dollar'],
    'OM':['Oman','OMN','968','OMR','Omani Rial'],
    'PA':['Panama','PAN','507','USD','United States Dollar'],
    'PE':['Peru','PER','51','PEN','Peruvian Sol'],
    'PF':['French Polynesia','PYF','689','XPF','CFP Franc'],
    'PG':['Papua New Guinea','PNG','675','PGK','Papua New Guinea Kina'],
    'PH':['Philippines','PHL','63','PHP','Philippine Peso'],
    'PK':['Pakistan','PAK','92','PKR','Pakistani Rupee'],
    'PL':['Poland','POL','48','PLN','Polish Zloty'],
    'PM':['Saint Pierre and Miquelon','SPM','508','EUR','European Euro'],
    'PN':['Pitcairn Islands','PCN','870','NZD','New Zealand Dollar'],
    'PR':['Puerto Rico','PRI','1787','USD','United States Dollar'],
    'PS':['Palestine','PSE','970','ILS','Israeli New Shekel'],
    'PT':['Portugal','PRT','351','EUR','European Euro'],
    'PW':['Palau','PLW','680','USD','United States Dollar'],
    'PY':['Paraguay','PRY','595','PYG','Paraguayan Guarani'],
    'QA':['Qatar','QAT','974','QAR','Qatari Riyal'],
    'RE':['Reunion Island','REU','262','EUR','European Euro'],
    'RO':['Romania','ROU','40','RON','Romanian Leu'],
    'RS':['Serbia','SRB','381','RSD','Serbian Dinar'],
    'RU':['Russia','RUS','7','RUB','Russian Ruble'],
    'RW':['Rwanda','RWA','250','RWF','Rwandan Franc'],
    'SA':['Saudi Arabia','SAU','966','SAR','Saudi Arabian Riyal'],
    'SB':['Solomon Islands','SLB','677','SBD','Solomon Islands Dollar'],
    'SC':['Seychelles','SYC','248','SCR','Seychelles Rupee'],
    'SD':['Sudan','SDN','249','SDG','Sudanese Pound'],
    'SE':['Sweden','SWE','46','SEK','Swedish Krona'],
    'SG':['Singapore','SGP','65','SGD','Signapore Dollar'],
    'SH':['Saint Helena','SHN','290','SHP','Saint Helena Pound'],
    'SI':['Slovenia','SVN','386','EUR','European Euro'],
    'SJ':['Svalbard and Jan Mayen','SJM','47','NOK','Norwegian Krone'],
    'SK':['Slovakia','SVK','421','EUR','European Euro'],
    'SL':['Sierra Leone','SLE','232','SLL','Sierra Leonean Leone'],
    'SM':['San Marino','SMR','378','EUR','European Euro'],
    'SN':['Senegal','SEN','221','XOF','West African CFA Franc'],
    'SO':['Somalia','SOM','252','SOS','Somalia Shilling'],
    'SR':['Suriname','SUR','597','SRD','Surinamese Dollar'],
    'SS':['South Sudan','SSD','211','SSP','South Sudanese Pound'],
    'ST':['Sao Tome and Principe','STP','239','STN','Sao Tome and Principe Dobra'],
    'SV':['El Salvador','SLV','503','USD','United States Dollar'],
    'SX':['Sint Maarten','SXM','1721','ANG','Netherlands Antillean Guilder'],
    'SY':['Syria','SYR','963','SYP','Syrian Pound'],
    'SZ':['Eswatini','SWZ','268','SZL','Swazi Lilangeni'],
    'TC':['Turks and Caicos Islands','TCA','1649','USD','United States Dollar'],
    'TD':['Chad','TCD','235','XAF','Central African CFA Franc'],
    'TF':['Territory of the French Southern Antratic Lands','ATF','262','EUR','European Euro'],
    'TG':['Togo','TGO','228','XOF','West African CFA Franc'],
    'TH':['Thailand','THA','66','THB','Thai Baht'],
    'TJ':['Tajikistan','TJK','992','TJS','Tajikistani Somoni'],
    'TK':['Tokelau','TKL','690','NZD','New Zealand Dollar'],
    'TL':['Timor-Leste (East Timor)','TLS','670','USD','United States Dollar'],
    'TM':['Turkmenistan','TKM','993','TMT','Turkmen Manat'],
    'TN':['Tunisia','TUN','216','TND','Tunisian Dinar'],
    'TO':['Tonga Islands','TON','676','TOP','Tongo Pa\'anga'],
    'TR':['Turkey','TUR','90','TRY','Turkish Lira'],
    'TT':['Trinidad and Tobago','TTO','1868','TTD','Trindad and Tobago Dollar'],
    'TV':['Tuvalu','TUV','688','AUD','Australian Dollar'],
    'TW':['Taiwan','TWN','886','TWD','New Taiwan Dollar'],
    'TZ':['Tanzania','TZA','255','TZS','Tanzanian Shilling'],
    'UA':['Ukraine','UKR','380','UAH','Ukrainian Hryvnia'],
    'UG':['Uganda','UGA','256','UGX','Ugandan Shilling'],
    'UM':['United States Minor Outlying Islands','UNI','268','USD','United States Dollar'],
    'US':['United States','USA','1','USD','United States Dollar'],
    'UY':['Uruguay','URY','598','UYU','Uruguanyan Peso'],
    'UZ':['Uzbekistan','UZB','998','UZS','Uzbekistani Som'],
    'VA':['Holy See (Vatican City)','VAT','39','EUR','European Euro'],
    'VC':['Saint Vincent and the Grenadines','VCT','1784','XCD','East Caribbean Dollar'],
    'VE':['Venezuela','VEN','58','VES','Venezuelan Bolivar'],
    'VG':['British Virgin Islands','VGB','1284','USD','United States Dollar'],
    'VI':['US Virgin Islands','VIR','1340','USD','United States Dollar'],
    'VN':['Vietnam','VNM','84','VND','Vietnamese Dong'],
    'VU':['Vanuatu','VUT','678','VUV','Vanuatu Vatu'],
    'WF':['Wallis and Futuna','WLF','681','XPF','CPF Franc'],
    'WS':['Samao','WSM','685','WST','Samoan Tala'],
    'XK':['Kosovo','UNK','383','EUR','European Euro'],
    'YE':['Yemen','YEM','967','YER','Yemeni Rial'],
    'YT':['Mayotte','MYT','262','EUR','European Euro'],
    'ZA':['South Africa','ZAF','27','ZAR','South African Rand'],
    'ZM':['Zambia','ZMB','260','ZMW','Zambian Kwacha'],
    'ZW':['Zimbabwe','ZWE','263','USD','United States Dollar']}
'''def place(lay):
    fnam,enam,lnam,male,female,add,con,ph,city,state,date,b17,bb4,snam,scit,sadd,ssta,scon,sph,scode,gen,cus,semail,widgets,gui,core=lay
    fnam.setGeometry(160,30,200,35);fnam.setToolTip('First Name must start with first letter');fnam.show();fnam.setFocus()               
    lnam.setGeometry(520,30,200,35);lnam.show();lnam.setToolTip('Last Name must start with capital letter')
    enam.setGeometry(170,70,250,35);enam.show();enam.setToolTip('Use a valid Email Address')
    add.setGeometry(180,150,250,55);add.show();add.setToolTip('Use an existing home address')
    city.setGeometry(520,150,200,35);city.show();city.setToolTip('Input an existing Town/City')
    state.setGeometry(100,210,200,35);state.show();state.setToolTip('Input an existing State')
    con.setGeometry(100,110,170,35);con.show();ph.setGeometry(280,110,160,35);ph.show();ph.setToolTip('Enter a valid Phone Number')
    male.setGeometry(550,110,100,35);female.setGeometry(650,110,100,35);male.show();female.show()    
    fnam.editingFinished.connect(lambda:fnam.setAlignment(core.Qt.AlignCenter))
    lnam.editingFinished.connect(lambda:lnam.setAlignment(core.Qt.AlignCenter))
    enam.editingFinished.connect(lambda:enam.setAlignment(core.Qt.AlignCenter))
    con.editTextChanged.connect(lambda:con.setAlignment(core.Qt.AlignCenter));ph.editingFinished.connect(lambda:ph.setAlignment(core.Qt.AlignCenter))
    state.editingFinished.connect(lambda:state.setAlignment(core.Qt.AlignCenter))
    city.editingFinished.connect(lambda:city.setAlignment(core.Qt.AlignCenter))
    date.setDisplayFormat('MMM  dd  yyyy');date.setGeometry(600,70,155,35);date.show();date.setCalendarPopup(True);date.setAlignment(core.Qt.AlignCenter);date.setMaximumDate(b17);date.setDate(b17);date.setMinimumDate(bb4)
    snam.setGeometry(105,35,200,35);snam.show();snam.editingFinished.connect(lambda:snam.setAlignment(core.Qt.AlignCenter));snam.setToolTip('Input Store Name')
    sadd.setGeometry(110,120,250,55);sadd.show();sadd.setToolTip('Input the existing Store Address')
    scit.setGeometry(460,120,200,35);scit.show();scit.editingFinished.connect(lambda:scit.setAlignment(core.Qt.AlignCenter));scit.setToolTip('Input Store City')
    ssta.setGeometry(100,180,200,35);ssta.show();ssta.editingFinished.connect(lambda:ssta.setAlignment(core.Qt.AlignCenter));ssta.setToolTip('Input Store State')
    scon.setGeometry(100,77,175,35);scon.show();scon.editTextChanged.connect(lambda:scon.setAlignment(core.Qt.AlignCenter))
    sph.setGeometry(280,77,160,35);sph.show();sph.editingFinished.connect(lambda:sph.setAlignment(core.Qt.AlignCenter));sph.setToolTip('Input the valid Store Phone Number')
    semail.setGeometry(510,35,250,35);semail.show();semail.editingFinished.connect(lambda:semail.setAlignment(core.Qt.AlignCenter));semail.setToolTip('Input a valid Store Email Address')
    scode.setGeometry(150,220,200,35);scode.show();scode.editingFinished.connect(lambda:scode.setAlignment(core.Qt.AlignCenter));scode.setToolTip('Store Code must contain only 3 capital letters first than 3 numbers')
    gen.setGeometry(390,220,160,35);gen.show();gen.setFont(gui.QFont('Champagne & Limousines',15))    
    cus.clicked.connect(lambda _:scode.setEnabled(True))
    cus.setGeometry(590,220,160,35);cus.show();cus.setFont(gui.QFont('Champagne & Limousines',15))
    fnam.editingFinished.connect(lnam.setFocus);fnam.setPlaceholderText('Enter First Name')#;fnam.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    lnam.editingFinished.connect(enam.setFocus);lnam.setPlaceholderText('Enter Last Name')#;lnam.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    enam.editingFinished.connect(date.setFocus);enam.setPlaceholderText('Enter Email Address')#;enam.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    add.setPlaceholderText('Enter Home Address')#;add.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    city.editingFinished.connect(state.setFocus);city.setPlaceholderText('Enter City')#;city.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    state.editingFinished.connect(snam.setFocus);state.setPlaceholderText('Enter State')#;state.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    con.editTextChanged.connect(ph.setFocus);con.setPlaceholderText('Select Country Code')#;con.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    ph.editingFinished.connect(add.setFocus);ph.setPlaceholderText('Enter Phone')#;ph.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    #date.editingFinished.connect(bcc.setFocus);date.setPlaceholderText('Enter Date of Birth');date.setStyleSheet('border:2px;border-radius:20px')
    snam.editingFinished.connect(semail.setFocus);snam.setPlaceholderText('Enter Store Name')#;snam.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    sadd.setPlaceholderText('Enter Store Address')#;sadd.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    scit.editingFinished.connect(ssta.setFocus);scit.setPlaceholderText('Enter City')#;scit.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    ssta.editingFinished.connect(scode.setFocus);ssta.setPlaceholderText('Enter State')#;ssta.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    scon.editTextChanged.connect(sph.setFocus);scon.setPlaceholderText('Select Country Code')#;scon.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    sph.editingFinished.connect(semail.setFocus);sph.setPlaceholderText('Enter Phone')#;sph.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    semail.editingFinished.connect(scon.setFocus);semail.setPlaceholderText('Enter Email Address')#;semail.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
    scode.editingFinished.connect(gen.setFocus);scode.setPlaceholderText('Enter Store Code')#;scode.setStyleSheet('background-color:white;border:2px black;border-radius:20px')
'''