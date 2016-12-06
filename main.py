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
#from kivy.uix.camera import Camera
from plyer import camera
from kivy.core.window import Window

Builder.load_string(
'''
<StartScreen>:
	GridLayout:
		cols: 2
		Button:
			# text: "Button 1"
			on_press: root.manager.current = "camera"
			background_color: (0,1,0,0.5)
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'icon.png'
					pos: self.pos
					size: self.size
		Button: 
			# text: "Button 2"
			background_color: (0,1,0,0.5)
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'music_icon.png'
					pos: self.pos
					size: self.size
		Button:
			# text: "Button 3"
			background_color: (0,1,0,0.5)
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'gallery.png'
					pos: self.pos
					size: self.size
		Button:
			text: "Button 4"
			background_color: (0,1,0,0.5)

<CameraScreen>:
	BoxLayout:
		orientation: "vertical"
		Camera:
			id: 'camera'
			resolution: (1024, 1024)

		Button:
			# text: "Menu"
			size_hint: None,None
			width: root.width*0.15
			height: '48dp'
			background_color: 0, 1, 0, 0.5
			on_press: root.manager.current = "start"
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'back.png'
					pos: self.pos
					size: self.size

		Button:
			# text: "Capture photo"
			size_hint: None, None
			width: root.width*0.15
			height: '65dp'
			background_color: 255, 255, 255, 0.3
			on_press: root.click_pic()
			
			pos: self.parent.x*0.25, self.parent.y
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image: 
					source: 'capture.png'
					pos: self.pos
					size: self.size
		# Label: 
		# 	text: "1"
		# 	size_hint_y: None
		# 	width: root.width*0.5
		# 	height: '48dp'



''')

class StartScreen(Screen):
	pass
class CameraScreen(Screen):
	
	# def changei(x):
	# 	return str(int(x) + 1)
	
	def click_pic(self):
		Window.screenshot(name="example.jpeg")


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name="start"))
sm.add_widget(CameraScreen(name="camera"))

class CameraApp(App):
	sm.current = "start"
	def build(self):
		return sm
CameraApp().run()