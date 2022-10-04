# web-hpg
  Калькулятор профиля питания растений(логика взята из wega-hpg) доступен по ссылке https://calc.progl.su
  Взаимодейтсвует с вега-миксером, может находится в экосистеме вега, подробнее можно почитать на вики https://calc.progl.su/wiki/

# Установка и апдейт одной командой как компонент
  wget --no-cache -O - https://raw.githubusercontent.com/WEGA-project/web-hpg/main/install_for_wega.sh | bash 
  Внимание, для корректной работы инстаоятора нужен установленный wega-server 

# Установка и апдейт для персонального пользования - нужен установленный python3
  git clone https://github.com/WEGA-project/web-hpg
  python manage.py migrate
  python manage.py runserver 
  переходите в бразуер по ссылке  127.0.0.1:8000
  
