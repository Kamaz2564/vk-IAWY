U
    Ǻ[^bA  �                
   @   s�  d dl Z d dlZd dlZd dlZd dlmZ d dlmZ edd�Ze�	� Z
edkr^e�d� n
e�d� d	d
� Zdd� Zdd� Zdd� Zdd� Ze�  ee
�d kr�ed�Z
zee
� e�e
� e��  W n"   ed� ed� e�  Y nX n�ed�Zedk�s
edk�ree
�Ze��  n�edk�s0edk�r�ed�Z
z0ee
� e��  edd�Ze�e
� e��  W n"   ed� ed� e�  Y nX ned� e�  e�d� d ZdZe�s�edk�r�e�d� n
e�d� e�  d Zed k�r�ed� ned�e�� ed �Zed!k�r�edk�r(e�d� n
e�d� e�  ed"�Zed#� e�d$� eee�Zej j!ed%�Z"e"d  d& Z#e"d  d' Z$e#d( e$ Zej%j!ed)�Z&e&d* Z'ed+�e�� ed� ed,�Z(�q�ed-k�r$ed k�r�e�  �q�ed(� ej j!ed.d/�Z"ed0e# d1 e$ d2 � ed� e"d  d3 d4k�r8ed5� ned6� ed� e"d  d7 d8k�rded9� ned:� ed� e"d  d; d4k�r�ed<� n$e"d  d; d=k�r�ed>� ned?� ed� d@e"d  k�r�edAe"d  d@ dB  � ed� dCe"d  k�redDe"d  dC dB  � ed� ed,�Z(�q�edEk�r�ed k�rBe�  �q�d Z)d4Z*d Z+d Z,ee'k �rRe�d$� ej j!e-e&dF e �d%�Z"dGe"d  k�r�e+d4 Z+n�e"d  d7 dk�r>e�dH� ej%j.e&dF e edIdJ�Z/e/d* d k�rFe�dK� ej j!e&dF e d%� e"d  d& Z0e"d  d' Z1e0d( e1 Z2edLe2 dM e � e,d4 Z,ne)d47 Z)ed47 Z�qRe,d k�r�edNe-e� dO e-e)� � edP� n6e,d k�r�edNe-e� dO e-e)� � edQe-e,� � ed� ed,�Z(�q�edRk�r�ed k�r�e�  �q�edS� ed� g Z3edT��4� Z3edU� ee3�Z5d Z+d4Z*d Z,ee5k �r�e�d$� ej%j.e3e edV�Z"ej j!e3e d%�Z/e/d  d& Z0e/d  d' Z1e0d( e1 Z2ed4 Ze"d* d4k�r&edLe dM e2 � e,d4 Z,�q&e,d k�r�edW� ed� ed,�Z(�q�edXk�
r�ed k�r�e�  �q�edY� ed �Zed!k�rreee�Z6i Z7e7�8dZd[� e6dF D �� g Z9d Z:d Z;e7�<� D ]�Z=z>e�dH� e=d  Z>e=d4 Z?d\Z@ejAjBee>d]e?d^�ZBe:d4 Z:W n eCk
�r�   d ZBY nX eBd_ d4k�rRe9�Dd`�e=d4 e=d  �� eda� edb�e=d4 e=d  �� e�d4� e;d4 Z;ed� �qRe;d k �r:edc� edde-e:� � n$edee-e;� df � edde-e:� � ed� ed,�Z(�q�ed-k�
r�d Z)d ZEd ZFd4ZGd Z d ZHee'k �
rDej j!e&dF e d%�Z"dGe"d  k�r�e+d4 Z+�nZe"d  d7 dk�
r e�dK� ejIj!e&dF e dgdh�ZIeId* ZJe d47 Z edie"d  d&  d( e"d  d'  � edj�e"d  d& e"d  d' �� eJd k�
reEeJk�
reEdkk �
re&dF e ZKeIdF eEd4  dl ZLejAjBedmeKeLdn�ZMe�d$� eEd47 ZEeFd47 ZFeMd_ d4k�	r`edoe-eK� dp e-eK� dq e-eL� dr ds e-eK� dt du � �	q`neHd47 ZHne)d47 Z)ed47 Zd ZEd ZJed� �q�edv� edwe-e5� dx e-eF� � edye-eH� � ed� ed,�Z(nedzk�r�dZ�q�ed{k�r�ed k�
r�e�  �q�ej6jNedkd|�Z"ed}� z�eOe"d* �Z5ee5k �r�e�d~� e"dF e d ZPe-e"dF e d� �ZQe-e"dF e d� �ZRed� ed�� ed��e�Sd�e�TeOeP����� ed��eQeR�� ed��e"dF e d� �� ed� ed47 Z�
q�W n   ed�� dZY nX ed� ed,�Z(�q�ed�k�r�ed k�r�e�  �q�eee�Z6d4Z5i Z7e7�8d�d[� e6dF D �� e7�<� D ]TZ=e�d4� ed��e-e5��� ed��e=d4 e=d  �� ed� e5d47 Z5e�dH� �qed� ed,�Z(nRedzk�r�ed�d�d�d��ZUeU�	� ZVeeV� ed� ed,�Z(ned�� ed� ed,�Z(�q�dS )��    N)�platform)�datetimezaddit/tokenzr+Zwin32�cls�clearc                 C   s�   t j| d�}t j|ddd�}t�dd�}|jjd| |d� t�d	� z8|jj	ddd
�d d d }|jj
|dd� td� W n   td� t�  Y nX t j|ddd�S )N)Zaccess_tokenz5.103Zru)�vZlang�   �@   i��")�user_id�messageZ	random_id皙�����?)r	   �count�itemsr   �id)Zmessage_idsZdelete_for_allu@   [32m[√] Вы успешно авторизовались [0mz[31m[!] Invalid Token[0m)�vkZSessionZAPI�random�randintZmessages�send�time�sleepZ
getHistory�delete�print�quit)�tokenZsession�apiZrandZmg_id� r   �vk-seeker.py�auth   s    
r   c                  C   s   t d� t d� td�} d S )Nu4   [31m[!] Сначала введите жертву!� �K   [32mЧтобы вернуться назад, нажмите 'ENTER': [0m)r   �input)�backr   r   r   �	gettarget   s    r!   c                 C   sR   | }d| kr| � d�d }|�dd��� s>|jj|d�d }n|�dd�}t|�S )Nzvk.com/�/�����r   r   )Zscreen_nameZ	object_id)�split�replace�isdigitZutilsZresolveScreenName�int)�linkr   �targetr   r   r   �getlink!   s    r*   c                 C   sH   |j j| dd�d d }dd� |D �}i }|jjdd�|�d	d
d�}|S )Nr   )r	   Zextended�groupsr   c                 S   s   g | ]}d t |� �qS )�-)�str��.0�xr   r   r   �
<listcomp>-   s     zgetwall.<locals>.<listcomp>zpost, audioz, �d   �
   )�filtersZ
source_idsr   Ztimeout)�usersZgetSubscriptions�newsfeed�get�join)r)   r   Zsubscriptions_listZgroups_list�postsr6   r   r   r   �getwall+   s     �r:   c                  C   s"   t �dd�} td�t| ��� d S )N�   �$   u�  [{}m                                                                                                                                                                                                       

	 ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄         ▄ ▄         ▄ 
	▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌       ▐░▐░▌       ▐░▌
	 ▀▀▀▀█░█▀▀▀▀▐░█▀▀▀▀▀▀▀█░▐░▌       ▐░▐░▌       ▐░▌
	     ▐░▌    ▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▌
	     ▐░▌    ▐░█▄▄▄▄▄▄▄█░▐░▌   ▄   ▐░▐░█▄▄▄▄▄▄▄█░▌
	     ▐░▌    ▐░░░░░░░░░░░▐░▌  ▐░▌  ▐░▐░░░░░░░░░░░▌
	     ▐░▌    ▐░█▀▀▀▀▀▀▀█░▐░▌ ▐░▌░▌ ▐░▌▀▀▀▀█░█▀▀▀▀ 
	     ▐░▌    ▐░▌       ▐░▐░▌▐░▌ ▐░▌▐░▌    ▐░▌     
	 ▄▄▄▄█░█▄▄▄▄▐░▌       ▐░▐░▌░▌   ▐░▐░▌    ▐░▌     
	▐░░░░░░░░░░░▐░▌       ▐░▐░░▌     ▐░░▌    ▐░▌     
	 ▀▀▀▀▀▀▀▀▀▀▀ ▀         ▀ ▀▀       ▀▀      ▀                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
	[0mTermux-Utility				vk: @terutil

	)r   r   r   �formatr-   )Zcolorr   r   r   �table7   s    �r>   u1   [33m[#] Введите свой токен: [0mr   z[31mError 1[0muk   [33m[#] Использовать сохраненные данные авторизации? <Y / N>: [0m�y�Y�n�N�wz[31m[!] Invalid TokenFuQ  [34m
[1] Указать жертву
[33m-------->[36mNONE[34m

[2] Информация о пользователе
[3] Кто скрывет
[4] Скрытые друзья
[5] Поиск лайков
[6] Где упоминали
[7] Посмотреть ленту

-----------------------------

[0] Информация
		
[0muP  [34m
[1] Указать жертву
[33m--------> [36m{}[34m

[2] Информация о пользователе
[3] Кто скрывет
[4] Скрытые друзья
[5] Поиск лайков
[6] Где упоминали
[7] Посмотреть ленту

-----------------------------

[0] Информация
		
[0mz[33m=> [0m�1u<   [33m[#] Введите ссылку на жертву: [0mu!   [34m[~] Проверка...[0m
r   )�user_ids�
first_name�	last_name� )r	   r   uf   [33m[~] Проверка завершена.
[32m[√] Жертва добавлена: [36m{}[32mr   �2zcountry, sex, online)rE   Zfieldsu   [33mИмя:        	[36mu   
[33mФамилия: 	[36mz[0mZonliner   u$   [33mСтатус:  	[32mOnline[0mu%   [33mСтатус:  	[31mOffline[0mZ	is_closedTu+   [33mПрофиль: 	[31mЗакрыт[0mu+   [33mПрофиль: 	[32mОткрыт[0mZsexu)   [33mПол:     	[35mЖенский[0m�   u)   [33mПол:     	[34mМужской[0mu'   [33mПол:     	[0mНе указанZcountryu   [33mСтрана:  	[0m�titleZcityu   [33mГород:   	[0m�3r   Zdeactivatedg      �?i�  )r	   �qr   g333333�?u   [32m[√] [0mu   [32m скрывает [0mu.   [33m[~] Проверено друзей: [0mu/   
[33m[~] Скрытых профилей: [0mub   [31m[!] Друзья, скрывающие данную страницу не найдены![0muQ   [32m[√] Друзей, скрывающих данную страницу: [0m�4u�  [31mПРИМЕЧАНИЕ: [0m
Сюда нужно ввести ID пользователя, которого вы
подозреваете, что ваша жертва его скрывает.
Страница подозреваемого должны быть не закрыта!
Подозреваемых может быть несколько, вводить через [31mПРОБЕЛ![0muD   [33m[#] Введите ID подозреваем(ых/ого): [0mz 
 )r	   rM   uH   [31m[!] Никто из подозреваемых не скрыт![0m�5uj   [34m
[1] В ленте
[2] На фото друзей

-----------------------------

[0] Назад
[0mc                 C   s   i | ]}|d  |d �qS ��post_idZ	source_idr   r.   r   r   r   �
<dictcomp>8  s      rR   �   �post)r	   �item_id�type�owner_id�likedzvk.com/wall{0}_{1}z"[33m-----------------------------zvk.com/wall{}_{}u?   [31m[!] Лайкнутые посты не надйены![0mu.   [33m[~] Проверено постов: [0mu   [32m[√] Найдено: [0mu&    [32mлайкнутых постов!Zprofile)rW   Zalbum_idz[33m                   z@[32m-----------------------------------------------------------�2   r   Zphoto)r	   rV   rW   rU   u$   [36mСсылка: https://vk.com/idz?z=photo�_z%2ZFalbumz_0%2ZFrevu7   [32m[√] Сканирование завершено!u2   [33m[~] Сканировано друзей: [0mu:   
[33m[~] Сканировано фотографий: 0mu1   [33m[~] Аккаунтов без фото: [0m�0�6)rW   r   u@   [32m[√] Поиск комментариев начат...[0mg�������?�date�to_idrQ   z>[32m-----------------------------------------------------[0mu   [33mДата: [0m{}z%D %H:%Mu4   [33mСсылка: [36mhttps://vk.com/wall{}_{}[0mz[33m{}[0m�textu8   [31m[!] Комментарии не найдены![0m�7c                 C   s   i | ]}|d  |d �qS rP   r   r.   r   r   r   rR   �  s      z+[33m-----------------({})-----------------z[32mvk.com/wall{}_{} [0mz
addit/help�rzutf-8)�encodingz[31m[!] Invalid Task)Wr   r   r   �os�sysr   r   �open�f�readr   �systemr   r!   r*   r:   r>   �lenr   �write�closer   r   Ztaskr   r)   Zdone�ir=   �namer(   r   r5   r7   ZresponserF   rG   ZfriendsZfriends_listZfriendcountr    �closed�loadZudalenZcountsr-   �searchZ	responsedZfirst_name1Z
last_name1Zname1Zsuspectr$   r   r6   r9   �updateZliked_postsZpostedZlikedsr   rT   ZitemIDZownerIDZtimeOutZlikesZisLiked�	Exception�appendZi2ZphotoscZdowZnophotoZphotosZcountprW   rU   rX   ZgetMentionsr'   Ztsr^   rQ   �strftime�	localtime�hZhelr   r   r   r   �<module>   sV   











�































�





$ 

F






 







