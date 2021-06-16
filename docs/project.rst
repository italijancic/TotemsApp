Project Description
====================
The global goal of project is desing and develop an Smart Totems
whit the next main functionalities:

- Detect register personal of institution and authorize acces to building
- Measure body temperature
- Send information about user, and temperature to server
- If the acces is enable:
  - Notify to the user
  - Send data data to server
  - Server must to store all data on a data base
- At the end of the day an administrator of app can see the names a data of all person that have acces to building and his correspondient corporal temperature.

To reach this the entire project is composed by:

- Smart Totems: Embedded hardware
- Web Application:
  - Bak-end
  - Front-end

Smart Totems
============
Bascically is the hardware of the develop. Consist on metal structure whit the embedded electronic inside.
The embedded system must to contain:

- MCU
- Wirless conectivity
- Infrared Sensor temperature: the selected sensor for the application is MLX90614
- HMI, composed of:
    - LCD 16X2
    - Buzzer
    - Two leds to indicate states of the global proces

Web Application
===============

Back-end
--------

Web Server: Django
^^^^^^^^^^^^^^^^^^

Data Base: MongoDB
^^^^^^^^^^^^^^^^^^

MQTT Brocker: Mosquitto
^^^^^^^^^^^^^^^^^^^^^^^


Front-end
---------


