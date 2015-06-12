# slackbot-workout
Traduccion de slackbot-workout en español. Ahora podras disfrutar en tu Slack de un bot que anuncie ejercicios aleatoriamente.
Proyecto original en https://github.com/brandonshin/slackbot-workout
<img src = "https://ctrlla-blog.s3.amazonaws.com/2015/Jun/Screen_Shot_2015_06_10_at_5_57_55_PM-1433984292189.png" width = 500>


# Instrucciones

1. Clona el repositorio.

    `$ git clone https://github.com/Mangu93/slackbot-workout.git'

2. Ve a tu pagina principal de Slack, https://{yourgroup}.slack.com/home y haz click en **Integrations** en la barra lateral.

    <img src = "https://ctrlla-blog.s3.amazonaws.com/2015/Jun/Screen_Shot_2015_06_05_at_7_21_33_PM-1433557303531.png" width = 300>

3. Desplazate hacia abajo hasta encontrar Slack API y Slackbot. Necesitaras acceso a ambos
    <img src="https://ctrlla-blog.s3.amazonaws.com/2015/Jun/Screen_Shot_2015_06_05_at_7_19_44_PM-1433557206307.png" width = 500>

4. En Slack API Page selecciona WebAPI en la barra lateral, desplazate hacia abajo y registra un auth token. Apuntalo para mas tarde.
    <img src="https://ctrlla-blog.s3.amazonaws.com/2015/Jun/Screen_Shot_2015_06_05_at_7_00_24_PM-1433557433415.png" width = 500>

5. En Slackbot registra una integracion y deberias ver algo asi. __Asegurate de que apuntas el token, ejemplo `AizJbQ24l38ai4DlQD9yFELb`

    <img src="https://ctrlla-blog.s3.amazonaws.com/2015/Jun/Screen_Shot_2015_06_03_at_8_44_00_AM-1433557565175.png" width = 500>

6. Abre el archivo `slackbotExercise.py` y rellena  **URLTOKENSTRING** y **USERAUTHTOKEN** con los tokens de Slackbot Remote Control y Slack Web API respectivamente.

7. Si no tienes PIP instalado haz lo siguiente en tu terminal.
`$ sudo easy_install pip`

8. En la carpeta del proyecto haz lo siguiente desde la terminal

    `$ sudo pip install -r requirements.txt`

    `$ python slackbotExercise.py`
Ejecuta el script para empezar los ejercicios y pulsa ctrl+c para pararlo. ¡Espero que lo disfrutes!
