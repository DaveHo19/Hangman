from tkinter import * 

class MainImage:
    def __init__(self, location):
        #create a canvas based on root provided, and initial canvas size
        self.mainCanvas = Canvas(location, width=200, height=200)
        #insert canvas into root
        self.mainCanvas.pack()
        #list of images phases
        self.imageList = []
        self.imageList.append(PhotoImage(file='src/phase_0.png'))
        self.imageList.append(PhotoImage(file='src/phase_1.png'))
        self.imageList.append(PhotoImage(file='src/phase_2.png'))
        self.imageList.append(PhotoImage(file='src/phase_3.png'))
        self.imageList.append(PhotoImage(file='src/phase_4.png'))
        self.imageList.append(PhotoImage(file='src/phase_5.png'))
        self.imageList.append(PhotoImage(file='src/phase_6.png'))
        self.imageList.append(PhotoImage(file='src/phase_7.png'))
        #current image phases
        self.currImageID = 0
        #display image based on image phases
        self.imageCanvas = self.mainCanvas.create_image(0,0, anchor=NW, image=self.imageList[self.currImageID])
       
    
    def displayCanvasImage(self, imageId):
        #if image phases is less than minimum phases or exceed maximum phases, return null
        if (imageId < 0) or (imageId > 7):
            return
        #update display image based on image phases
        else:          
            self.currImageID = imageId
            self.mainCanvas.itemconfig(self.imageCanvas, image=self.imageList[self.currImageID])
            
    #release canvas from root
    def leaveGameImage(self):
        self.mainCanvas.pack_forget()
    

        