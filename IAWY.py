U
    �[^�A  �                
   @   s�  d dl Z d dlZd dlZd dlZd dlmZ d dlmZ edddd�Ze�	�  edd�Ze�
� Zed	krte�d
� n
e�d� dd� Zdd� Zdd� Zdd� Zdd� Ze�  ee�d k�red�Zzee�Ze�e� e�	�  W n"   ed� ed� e�  Y nX n�ed�Zedk�s"edk�r4ee�Ze�	�  n�edk�sHedk�r�ed�Zz0ee� e�	�  edd�Ze�e� e�	�  W n"   ed� ed� e�  Y nX ned� e�  e�d
� d Zd Ze�s�ed	k�r�e�d
� n
e�d� e�  d Zed k�r
ed!� ned"�e�� ed#�Zed$k�r�ed	k�r@e�d
� n
e�d� e�  ed%�Zed&� e�d'� eee�Zej j!ed(�Z"e"d  d) Z#e"d  d* Z$e#d+ e$ Zej%j!ed,�Z&e&d- Z'ed.�e�� ed� ed/�Z(�q�ed0k�r<ed k�r�e�  �q�ed+� ej j!ed1d2�Z"ed3e# d4 e$ d5 � ed� e"d  d6 d7k�rPed8� ned9� ed� e"d  d: d;k�r|ed<� ned=� ed� e"d  d> d7k�r�ed?� n$e"d  d> d@k�r�edA� nedB� ed� dCe"d  k�r�edDe"d  dC dE  � ed� dFe"d  k�r(edGe"d  dF dE  � ed� ed/�Z(�q�edHk�r�ed k�rZe�  �q�d Z)d7Z*d Z+d Z,ee'k �rje�d'� ej j!e-e&dI e �d(�Z"dJe"d  k�r�e+d7 Z+n�e"d  d: d k�rVe�dK� ej%j.e&dI e edLdM�Z/e/d- d k�r^e�dN� ej j!e&dI e d(� e"d  d) Z0e"d  d* Z1e0d+ e1 Z2edOe2 dP e � e,d7 Z,ne)d77 Z)ed77 Z�qje,d k�r�edQe-e� dR e-e)� � edS� n6e,d k�r�edQe-e� dR e-e)� � edTe-e,� � ed� ed/�Z(�q�edUk�r�ed k�re�  �q�edV� ed� g Z3edW��4� Z3edX� ee3�Z5d Z+d7Z*d Z,ee5k �r�e�d'� ej%j.e3e edY�Z"ej j!e3e d(�Z/e/d  d) Z0e/d  d* Z1e0d+ e1 Z2ed7 Ze"d- d7k�r>edOe dP e2 � e,d7 Z,�q>e,d k�r�edZ� ed� ed/�Z(�q�ed[k�
r�ed k�re�  �q�ed\� ed#�Zed$k�r�eee�Z6i Z7e7�8d]d^� e6dI D �� g Z9d Z:d Z;e7�<� D ]�Z=z>e�dK� e=d  Z>e=d7 Z?d_Z@ejAjBee>d`e?da�ZBe:d7 Z:W n eCk
�r�   d ZBY nX eBdb d7k�rje9�Ddc�e=d7 e=d  �� edd� ede�e=d7 e=d  �� e�d7� e;d7 Z;ed� �qje;d k �rRedf� edge-e:� � n$edhe-e;� di � edge-e:� � ed� ed/�Z(�q�ed0k�
r�d Z)d ZEd ZFd7ZGd Z d ZHee'k �
r\ej j!e&dI e d(�Z"dJe"d  k�r�e+d7 Z+�nZe"d  d: d k�
r8e�dN� ejIj!e&dI e djdk�ZIeId- ZJe d77 Z edle"d  d)  d+ e"d  d*  � edm�e"d  d) e"d  d* �� eJd k�
r.eEeJk�
r6eEdnk �
r6e&dI e ZKeIdI eEd7  do ZLejAjBedpeKeLdq�ZMe�d'� eEd77 ZEeFd77 ZFeMdb d7k�	rxedre-eK� ds e-eK� dt e-eL� du dv e-eK� dw dx � �	qxneHd77 ZHne)d77 Z)ed77 Zd ZEd ZJed� �q�edy� edze-e5� d{ e-eF� � ed|e-eH� � ed� ed/�Z(ned}k�r�d Z�q�ed~k�r�ed k�
r�e�  �q�ej6jNednd�Z"ed�� z�eOe"d- �Z5ee5k �r�e�d�� e"dI e d� ZPe-e"dI e d� �ZQe-e"dI e d� �ZRed� ed�� ed��e�Sd�e�TeOeP����� ed��eQeR�� ed��e"dI e d� �� ed� ed77 Z�
q�W n   ed�� d ZY nX ed� ed/�Z(�q�ed�k�r�ed k�r e�  �q�eee�Z6d7Z5i Z7e7�8d�d^� e6dI D �� e7�<� D ]TZ=e�d7� ed��e-e5��� ed��e=d7 e=d  �� ed� e5d77 Z5e�dK� �q2ed� ed/�Z(nRed}k�r�ed�d�dd�ZUeU�
� ZVeeV� ed� ed/�Z(ned�� ed� ed/�Z(�q�dS )��    N)�platform)�datetimezaddit/token�azutf-8)�encodingzr+Zwin32�cls�clearc                 C   s�   t j| d�}t j|ddd�}t�dd�}|jjd| |d� t�d	� z8|jj	ddd
�d d d }|jj
|dd� td� W n   td� t�  Y nX t j|ddd�S )N)Zaccess_tokenz5.103Zru)�vZlang�   �@   i��")�user_id�messageZ	random_id皙�����?)r   �count�itemsr   �id)Zmessage_idsZdelete_for_allu@   [32m[√] Вы успешно авторизовались [0mz[31m[!] Invalid Token[0m)�vkZSessionZAPI�random�randintZmessages�send�time�sleepZ
getHistory�delete�print�quit)�tokenZsession�apiZrandZmg_id� r   �vk-seeker.py�auth   s    
r   c                  C   s   t d� t d� td�} d S )Nu4   [31m[!] Сначала введите жертву!� �K   [32mЧтобы вернуться назад, нажмите 'ENTER': [0m)r   �input)�backr   r   r   �	gettarget   s    r#   c                 C   sR   | }d| kr| � d�d }|�dd��� s>|jj|d�d }n|�dd�}t|�S )Nzvk.com/�/�����r   r   )Zscreen_nameZ	object_id)�split�replace�isdigitZutilsZresolveScreenName�int)�linkr   �targetr   r   r   �getlink#   s    r,   c                 C   sH   |j j| dd�d d }dd� |D �}i }|jjdd�|�d	d
d�}|S )Nr   )r   Zextended�groupsr   c                 S   s   g | ]}d t |� �qS )�-)�str��.0�xr   r   r   �
<listcomp>/   s     zgetwall.<locals>.<listcomp>zpost, audioz, �d   �
   )�filtersZ
source_idsr   Ztimeout)�usersZgetSubscriptions�newsfeed�get�join)r+   r   Zsubscriptions_listZgroups_list�postsr8   r   r   r   �getwall-   s     �r<   c                  C   s"   t �dd�} td�t| ��� d S )N�   �$   u�  [{}m                                                                                                                                                                                                       

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

	)r   r   r   �formatr/   )Zcolorr   r   r   �table9   s    �r@   u1   [33m[#] Введите свой токен: [0mr   z[31mInvalid Token[0muk   [33m[#] Использовать сохраненные данные авторизации? <Y / N>: [0m�y�Y�n�N�wz[31m[!] Invalid TokenFuQ  [34m
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
r   )�user_ids�
first_name�	last_name� )r   r   uf   [33m[~] Проверка завершена.
[32m[√] Жертва добавлена: [36m{}[32mr    �2zcountry, sex, online)rG   Zfieldsu   [33mИмя:        	[36mu   
[33mФамилия: 	[36mz[0mZonliner	   u$   [33mСтатус:  	[32mOnline[0mu%   [33mСтатус:  	[31mOffline[0mZ	is_closedTu+   [33mПрофиль: 	[31mЗакрыт[0mu+   [33mПрофиль: 	[32mОткрыт[0mZsexu)   [33mПол:     	[35mЖенский[0m�   u)   [33mПол:     	[34mМужской[0mu'   [33mПол:     	[0mНе указанZcountryu   [33mСтрана:  	[0m�titleZcityu   [33mГород:   	[0m�3r   Zdeactivatedg      �?i�  )r   �qr   g333333�?u   [32m[√] [0mu   [32m скрывает [0mu.   [33m[~] Проверено друзей: [0mu/   
[33m[~] Скрытых профилей: [0mub   [31m[!] Друзья, скрывающие данную страницу не найдены![0muQ   [32m[√] Друзей, скрывающих данную страницу: [0m�4u�  [31mПРИМЕЧАНИЕ: [0m
Сюда нужно ввести ID пользователя, которого вы
подозреваете, что ваша жертва его скрывает.
Страница подозреваемого должны быть не закрыта!
Подозреваемых может быть несколько, вводить через [31mПРОБЕЛ![0muD   [33m[#] Введите ID подозреваем(ых/ого): [0mz 
 )r   rO   uH   [31m[!] Никто из подозреваемых не скрыт![0m�5uj   [34m
[1] В ленте
[2] На фото друзей

-----------------------------

[0] Назад
[0mc                 C   s   i | ]}|d  |d �qS ��post_idZ	source_idr   r0   r   r   r   �
<dictcomp>:  s      rT   �   �post)r   �item_id�type�owner_id�likedzvk.com/wall{0}_{1}z"[33m-----------------------------zvk.com/wall{}_{}u?   [31m[!] Лайкнутые посты не надйены![0mu.   [33m[~] Проверено постов: [0mu   [32m[√] Найдено: [0mu&    [32mлайкнутых постов!Zprofile)rY   Zalbum_idz[33m                   z@[32m-----------------------------------------------------------�2   r   Zphoto)r   rX   rY   rW   u$   [36mСсылка: https://vk.com/idz?z=photo�_z%2ZFalbumz_0%2ZFrevu7   [32m[√] Сканирование завершено!u2   [33m[~] Сканировано друзей: [0mu:   
[33m[~] Сканировано фотографий: 0mu1   [33m[~] Аккаунтов без фото: [0m�0�6)rY   r   u@   [32m[√] Поиск комментариев начат...[0mg�������?�date�to_idrS   z>[32m-----------------------------------------------------[0mu   [33mДата: [0m{}z%D %H:%Mu4   [33mСсылка: [36mhttps://vk.com/wall{}_{}[0mz[33m{}[0m�textu8   [31m[!] Комментарии не найдены![0m�7c                 C   s   i | ]}|d  |d �qS rR   r   r0   r   r   r   rT   �  s      z+[33m-----------------({})-----------------z[32mvk.com/wall{}_{} [0mz
addit/help�rz[31m[!] Invalid Task)Wr   r   r   �os�sysr   r   �open�f�close�readr   �systemr   r#   r,   r<   r@   �lenr!   r   �writer   r   Ztaskr+   Zdone�ir?   �namer*   r   r7   r9   ZresponserH   rI   ZfriendsZfriends_listZfriendcountr"   �closed�loadZudalenZcountsr/   �searchZ	responsedZfirst_name1Z
last_name1Zname1Zsuspectr&   r   r8   r;   �updateZliked_postsZpostedZlikedsr   rV   ZitemIDZownerIDZtimeOutZlikesZisLiked�	Exception�appendZi2ZphotoscZdowZnophotoZphotosZcountprY   rW   rZ   ZgetMentionsr)   Ztsr`   rS   �strftime�	localtime�hZhelr   r   r   r   �<module>   sZ   



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