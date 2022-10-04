echo "##########################################################"
echo "############# Install or Update WEGA-WEB-HPG #############"
echo "##########################################################"
echo "Create database"
if [ ! -d "/var/WEGA" ] 
then
    echo "cant find WEGA on /var/WEGA. Please install WEGA first" 
    exit 1
fi
mkdir -p /var/web-hpg/

git clone  https://github.com/WEGA-project/web-hpg.git /var/web-hpg
cd /var/web-hpg/wega-hpg/
MYSQL=$(which mysql)
DB_PASS=$(echo "<?php include '/var/WEGA/db.php'; echo \$password;" | /usr/bin/php)
echo "Create wega-hpg db name: $MAIN_DB_NAME"
SQL="CREATE DATABASE IF NOT EXISTS wegacalc;"
$MYSQL -uroot -p$DB_PASS -e "$SQL"
echo "Install python"
a2enmod proxy_http
apt-get install --yes --quiet --no-install-recommends python3-pip python3-venv build-essential libssl-dev libffi-dev python3-dev libmysqlclient-dev libev-dev python3-wheel
deactivate
rm -R /var/web-hpg/wega-hpg/venv
python3 -m venv /var/web-hpg/wega-hpg/venv
source /var/web-hpg/wega-hpg/venv/bin/activate
pip3 install wheel
pip3 install -r /var/web-hpg/wega-hpg/requirements.txt
chmod 744 /var/web-hpg/wega-hpg/entrypoint.sh
cp -f /var/web-hpg/wega-hpg/scripts/wega-hpg.service /etc/systemd/system/wega-hpg.service
chmod 664 /etc/systemd/system/wega-hpg.service
ln -s /var/WEGA/apache/wega-hpg.conf /etc/apache2/conf-enabled/
mkdir -p /var/log/gunicron/
a2enmod headers
python manage_prod.py collectstatic --noinput
touch /var/web-hpg/wega-hpg/WEGA_HPG_PASSWORD
WEGA_HPG_PASSWORD=$(cat /var/web-hpg/wega-hpg/WEGA_HPG_PASSWORD)
if [[ -n "$WEGA_HPG_PASSWORD" ]]; then
  echo "we already have it"
else
  echo "Generating new WEGA_HPG_PASSWORD"
  WEGA_HPG_PASSWORD=$(openssl rand -hex 12)
fi
# P_STRING="from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', 'admin@localhost.ru', '$WEGA_HPG_PASSWORD')"
# echo $P_STRING | python manage_prod.py shell
echo $WEGA_HPG_PASSWORD >/var/web-hpg/wega-hpg/WEGA_HPG_PASSWORD
echo "WEGA_DEFAULT_USER = 'admin@localhost.ru'" > /var/web-hpg/wega-hpg/project/default_user.py
echo "WEGA_DEFAULT_PASSWORD = '$WEGA_HPG_PASSWORD'" >> /var/web-hpg/wega-hpg/project/default_user.py
python manage_prod.py migrate --noinput

systemctl daemon-reload
systemctl enable wega-hpg.service
systemctl restart wega-hpg.service
systemctl reload apache2
git config --global --add safe.directory /var/WEGA
echo "##########################################################"
echo "################# WEGA-WEB-HPG IS READY  #################"
echo "##########################################################"

echo "WEGA-HPG: http://$(hostname -I | sed -e "s/\s$//g")/wega-hpg/"
echo "Внимание! Не требует авторизации для однопользовательского режима!"




