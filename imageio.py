import imageio
import scipy
 
def create_gif(gif_name, duration=0.5):
    frames = []
    for i in range(1,33):
        frames.append(imageio.imread(r"C:\Users\17503\Desktop\study\landuse\land ({i}).jpg".format(i=i)))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return
 
def main():
    gif_name = 'test.gif'
    duration = 0.9
    create_gif(gif_name, duration)
 
if __name__ == '__main__':
    main()