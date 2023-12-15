#  _1_ё

def wow(kompaniya, model, rangi, nomi, yili, narhi=None):


    laptop = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'nomi':nomi,
            'yil':yili,
            'narh':narhi}
    return laptop

shokolad1 = wow('Alpengold','Nestle',"Yong'oli",'Oq',2018)
shokolad2 = wow('Alpengold','Milka','Oreo','Kit kat',2016,1000)
shokoladlar = [shokolad1, shokolad2]
print('Dokonda  mavjud shokoladlar:')
for shirinlik in shokoladlar:
    if shirinlik['narh']:
        narh = shirinlik['narh']
    else:
        narh = "Noma'lum"
    print(f"{shirinlik['rang']} {shirinlik['model']}. Narhi: {narh}")


