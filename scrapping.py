from ScrapCults3D import *
from ScrapPinshape import *
from ScrapYeggi import *
from ScrapThingiverse import *
from ScrapCgtrader import *

# ScrapYeggi().start_scrapping()
try:
    ScrapThingiverse().start_scrapping()
    #ScrapCults3D().start_scrapping()
    #ScrapPinshape().start_scrapping()
    #ScrapCgtrader().start_scrapping()

except KeyboardInterrupt as e:
    print("Process canceled.")
