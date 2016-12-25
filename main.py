import time
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import ObjectProperty
from kivy.core.image import Image
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.lang import Builder
from kivy.app import App 
from kivy.uix.screenmanager import Screen, ScreenManager , FadeTransition
#from kivy.uix.camera import Camera
from plyer.facades import camera
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

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
					source: 'icon/icon.png'
					pos: self.pos
					size: self.size
		Button: 
			# text: "Button 2"
			on_press: root.manager.current = "audio"
			background_color: (0,1,0,0.5)
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'icon/music_icon.png'
					pos: self.pos
					size: self.size
		Button:
			# text: "Button 3"
			background_color: (0,1,0,0.5)
			on_press: root.manager.current = "gallery"
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'icon/gallery.png'
					pos: self.pos
					size: self.size
		Button:
			text: ""
			background_color: (0,1,0,0.5)
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'icon/credit.png'
					pos: self.pos
					size: self.size

<CameraScreen>:
	BoxLayout:
		orientation: "vertical"
		Camera:
			id: camera
			resolution: (1024, 1024)

		Button:
			size_hint: None,None
			width: '80dp'
			height: '80dp'
			pos: self.pos
			background_color: 0, 1, 0, 0.5
			on_press: root.manager.current = "start"
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'icon/back.png'
					pos: self.pos
					size: self.size
	
		Button:
			# text: "Capture photo"
			size_hint: None, None
			width: '80dp'
			height: '80dp'
			background_color: 255, 255, 255, 0.3
			on_press: root.click_pic()
			# pos_hint: 0.25	
			# pos: self.parent.x*0.25, self.parent.y
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image: 
					source: 'icon/capture.png'
					pos: self.pos
					size: self.size
		
<GalleryScreen>:
	GridLayout:
		orientation: 'vertical'
		cols: 1
		GridLayout:
			cols: 2
			padding: 5
			spacing: 400
			size_hint_y: None
			height: self.minimum_height
			Label: 
				text: "Gallery"
				font_size: 40
			Button: 
				text: "back"
				on_press: root.manager.current = "start"
				size_hint: None, None
				height: '40dp'
				width: '40dp'
		ScrollView:
			id: scroller
			# size_hint:None, None
			# size: 500, 320
	        # pos_hint: {'center_x': .5, 'center_y': .5}, 
	  #       do_scroll_x:False
			
			GridLayout:
				cols: 4

				padding: 10
				spacing: 10
				size_hint_y: None
				height: self.minimum_height
				id: gallery_layout
				
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '40dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'				
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'			
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
					height: '240dp'
				Image:
					source: 'pics/yash.jpg'
					size_hint_y: None
				
		# Button: 
		# 	on_press: root.AddImage()	

<AudioScreen>:
	GridLayout:
		cols: 1
		Button:
			text: "hello"
			on_press: root.define()
		Button: 
			id: btn
			text: "press"

''')
camera = ObjectProperty(None)
gallery_layout = ObjectProperty(None)
class StartScreen(Screen):
	pass
class AudioScreen(Screen):
	def define(self):
		print "entered into define"
		btn = self.ids['btn']
		btn.bind(on_press=self.playmusic)
 
	def playmusic(self,*args):
		print "played"
		s = SoundLoader.load('example.wav')
		print "hey executed"
		# sound.volume = 0.5
		# sound.play()	

class CameraScreen(Screen):
	
	# def changei(x):
	# 	return str(int(x) + 1)
	
	def click_pic(self):
		camera = self.ids['camera']
		timestr = time.strftime("%d-%m-%Y_%H:%M:%S")
		camera.export_to_png("IMG_" + timestr)
		print "Captured"
		print time.strftime("%d%m%Y_%H%M%S")
class GalleryScreen(Screen):
	# def __init__(self):
	# 	self.AddImage()
	def AddImage(self):
		gallery_layout = self.ids['gallery_layout']
		# for i in range(0,11):
		# 	im = Image(source='gallery.png')
		# 	gallery_layout.add_widget(im)


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name="start"))
sm.add_widget(CameraScreen(name="camera"))
sm.add_widget(GalleryScreen(name="gallery"))
sm.add_widget(AudioScreen(name="audio"))
class CameraApp(App):
	sm.current = "gallery"
	def build(self):
		return sm
CameraApp().run()