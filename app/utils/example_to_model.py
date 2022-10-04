import decimal
import logging
import os
import django
from pathlib import Path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from django.contrib.auth.models import User
from calc.models import PlantProfile, PlantTemplate

root = '../examples'
files_local = {}

PlantProfile.objects.all().delete()
PlantTemplate.objects.all().delete()


# PlantProfile.objects.filter(user = User.objects.get(pk=6)).delete()
a=0

from django.contrib.auth.models import User
try:
    User.objects.get(pk=1)
except Exception as e:
    User.objects.create_user('admin', )
    
    
def make_template(path, name, desc):
    global a
    a+=1
    
    # print('make_template path', path)
    with open(os.path.join(path), 'r') as f:
        data = f.read()
        create_kw = {'name': str(path[path.rfind('/')+1:])}
        for item in data.splitlines():
            if not item or item and item.startswith('date=') or item.find(' ;')>=0 :
                continue
            try:
                key, value = item.split('=')
                
                if key=="V":
                    create_kw['litres'] = float(value)
                    continue
                    
                if key == 'chkComplex':
       
                    if value=='TRUE':
                        create_kw['micro_calc_mode'] = "b"
                    else:
                        create_kw['micro_calc_mode'] = "u"
                    continue
                    
                if key == 'chK2SO4':
                    if value=='TRUE':
                        create_kw['calc_mode'] = 'K'
                        continue
                        
                if key == 'chMgNO3':
                    if value=='TRUE':
                        create_kw['calc_mode'] = 'Mg'
                        continue
                    
           
                
                for i in ['gml_fe', 'gml_mn', 'gml_b', 'gml_zn', 'gml_cu', 'gml_mo', 'gml_co',
                        'gml_si', 'gml_cano3', 'gml_kno3', 'gml_nh4no3', 'gml_mgno3', 'gml_mgso4', 'gml_k2so4',
                        'gml_kh2po4', 'gml_cacl2', 'gml_cmplx', 'gl_fe', 'gl_mn', 'gl_b', 'gl_zn',
                        'gl_cu', 'gl_mo', 'gl_co', 'gl_si', 'gl_cano3', 'gl_kno3', 'gl_nh4no3', 'gl_mgno3',
                        'gl_mgso4', 'gl_k2so4', 'gl_kh2po4', 'gl_cacl2', 'gl_cmplx', 'ml_cano3', 'gg_cano3',
                        'ml_kno3', 'gg_kno3', 'ml_nh4no3', 'gg_nh4no3', 'ml_mgno3', 'gg_mgno3', 'ml_cacl2',
                        'gg_cacl2',
                        'ml_mgso4', 'ml_kh2po4', 'ml_k2so4', 'ml_fe', 'ml_mn', 'ml_b', 'ml_zn', 'ml_cu', 'ml_mo',
                        'ml_co', 'ml_si', 'ml_cmplx',
                        'gg_mgso4', 'gg_kh2po4', 'gg_k2so4', 'gg_fe', 'gg_mn', 'gg_b', 'gg_zn', 'gg_cu', 'gg_mo',
                        'gg_co', 'gg_si', 'gg_cmplx']:
                    
                    if i.replace('_', '') == key.lower():
                        key = i
                        break
                    
                
                
                if key.lower() in PlantProfile.model_create_fields:
                    create_kw[key.lower()] = float(value)
            except Exception as e:
                logging.exception(e)
                pass
        create_kw['ec'] = 0
        create_kw['ppm'] = 0
        create_kw['user_id'] = 1
        pp = PlantProfile(**create_kw)
        owner = str(Path(path).parent).replace('../examples/', '')
        owner=owner[:owner.rfind('/')]
        if owner=='..':owner='root'
        plant_dict = {
            'name' : str(path[path.rfind('/') + 1:]).capitalize(), 'description' : desc, 'profile_owner' : owner
        }
        # t = PlantTemplate(name=str(path[path.rfind('/')+1:]), description=desc, profile_owner=owner)
        # t.save()
        # pp.template = t
        # pp.save()
        return {'plant_template':plant_dict,  'plant_profile':create_kw}

    print(f'total {a}')
for path, subdirs, files in os.walk(root):
    current_dir = None
    for name in files:
        dirname = path
        if dirname not in files_local:
            files_local[dirname] = {'description':'', 'files':[], 'name':name}
            
        if name.endswith('hpg'):
            # print(os.path.join(path, name))
            files_local[dirname]['files'].append(os.path.join(path, name))
        if name.endswith('md') or name.endswith('txt'):
            files_local[dirname]['description'] = os.path.join(path, name)
            # print(os.path.join(path, name))
items =[]
# print('files_local', files_local)
for key, item in files_local.items():
    desc = []
    if len(item['files']) ==0:
        continue
    if  item['description']:
        with open( item['description'], 'r') as f:
            desc = f.readlines()
    print(key, 'desc', len(desc), len(item['files']))
   
    for file in item['files']:
        # print(file)
        # if file=='../examples/for_test.hpg':
        #     items.append(make_template(file, item['name'], desc))

        items.append(make_template(file, item['name'], desc))


print(items)