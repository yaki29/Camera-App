from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.gridlayout import GridLayout 



from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.lang import Builder
from kivy.app import App 
from kivy.uix.screenmanager import Screen, ScreenManager , FadeTransition
from kivy.uix.camera import Camera

Builder.load_string(
'''
<StartScreen>:
	GridLayout:
		cols: 2
		Button:
			text: "Button 1"
			on_press: root.manager.current = "camera"
			background_color: (0,1,0,0.5)
		Button: 
			text: "Button 2"
			background_color: (0,1,0,0.5)
		Button:
			text: "Button 3"
			background_color: (0,1,0,0.5)
		Button:
			text: "Button 4"
			background_color: (0,1,0,0.5)

<CameraScreen>:
	BoxLayout:
		orientation: "vertical"
		Camera:
			id: 'camera'
			resolution: (650, 480)
		Button:
			text: "Menu"
			size_hint: None,None
			width: root.width*0.5
			height: '48dp'
			on_press: root.manager.current = "start"

		Button:
			text: "Front"
			size_hint: None,None
			width: root.width*0.5
			height: '48dp'


''')

class StartScreen(Screen):
	pass
class CameraScreen(Screen):
	pass

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name="start"))
sm.add_widget(CameraScreen(name="camera"))

class CameraApp(App):
	sm.current = "start"
	def build(self):
		return sm
CameraApp().run()