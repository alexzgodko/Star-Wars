# ���� ��������� "Star Wars"
##### `import pygame`

����������� ������� ���������� ����� ������ � ����������� ��������� �����/������.
�� ���� ����� ��������� ������ �������� ������ ���� ��� ������� ������.
��� ��������� ��������� � ������� ����������� ��� ����� ������� ��������������� ������� ���������.
������� ����� ����� �������� �� ����������. �� ��������� ��� ����������� ���� ��������������� ������� ���������.
���� ����: ������� ������������ ���������� �����, ������� �� ����������, ���� ������� ������� �� �����������.

## ������

* Class Player - ����������� �������
    1. image - �����������
    2. rect - ������������� �����������
    3. rect.centerx - ������� �� x
    4. rect.bottom - ������� �� y
    5. speedx - �������� �� x
    6. shield - ����� ������� 
    7. last_update - ��������� ����������
* Class Meteor - ��������
    1. image_orig - �����������
    2. image - ����� �����������, ������� ����� ��������� ������������ ������
    3. rect - ������������� �����������
    4. radius - ������ ���������
    5. rect.x - ��������� ������� �� x
    6. rect.y - ��������� ������� �� y (�� ��������� ������)
    7. speedx - �������� �� x (��-�� ���� ����� ��� ��������)
    8. speedy - �������� �� y (������������� ��� ������ �����)
    9. rot - ������� ���� �������� ������������ ������
    10. rot_speed - �������� ��������� ���� ��������
    11. last_update - ��������� ���������� 
* Class Bullet - ����, ������� �������� �������
    1. image - �����������
    2. rect - ������������� �����������
    3. rect.bottom - ������� �� y
    4. rect.centerx - ������� �� x
    5. speedy - �������� �� y (����� ����� �����)
* Class Explosion - ���������� �������� ��������� ���� � ��������
    size - 'lg': ��� �������� ���� � ����������, 'sm': ��� �������� ��������� � ��������
    image - ������� �����������
    rect - ������������� �����������
    rect.center - ����� ��������������
    frame - ����� �������� ����� ��������
    frame_rate - ������� �� ���������� ���� ���� �������� 
    last_update - ��������� ���������� 

��� ������������� ������� �������� ���������: `pygame.sprite.Sprite`.
��� �������� ����������� �������� � ������ ����������.
��� ���� � �������� ��� �������� ���������� � `pygame.sprite.Group()`.

## � ���� ���� 3 ���������:

1. Go Screen - ��������� ����� � ������������.
2. Game Over Screen - ����� �� ��������� �����. ���������� ������������ ���� � ������ "������ ���� ������".
3. Game - ���������� ����

## ������� ����:

Go Screen -> Game -> Game Over Screen -> Game -> Game Over Screen -> ...