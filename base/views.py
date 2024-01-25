from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Player,Duel,SinglesMatch,DoublesMatch
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .forms import DuelForm, SinglesMatchInlineFormSet, DoublesMatchInlineFormSet
from .forms import SinglesMatchInlineForm,DoublesMatchInlineForm
from selenium import webdriver
from io import BytesIO
from django.template.loader import get_template
from selenium import webdriver
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import base64
from io import BytesIO
import base64
from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

# Create your views here.

def home(request):
    players=Player.objects.all()
    context={'players':players,}
    return render(request,'base/home.html',context)

def players(request):
    players=Player.objects.all()
    context={'players':players}
    return render(request,'base/players.html',context)
def generate_graph(data, attribute):
    matplotlib.use('Agg')
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
    dates = [entry['date'] for entry in sorted_data]
    values = [entry[attribute] for entry in sorted_data]
    font_family = 'Arial'  
    with plt.xkcd():
        plt.rcParams['font.family'] = font_family  

        plt.figure(figsize=(8, 6))
        plt.plot(dates, values, marker='o', linestyle='-', label=f'{attribute.capitalize()} Data')
        plt.xlabel('Date')
        plt.ylabel(attribute.capitalize())  
        plt.title(f'{attribute.capitalize()} over Time')
        plt.legend()  


        graph_image = BytesIO()
        plt.savefig(graph_image, format='png')
        graph_image.seek(0)

        encoded_image = base64.b64encode(graph_image.read()).decode('utf-8')

        plt.close()  
    
    return encoded_image

def profile(request,pk):
    player=Player.objects.get(id=pk)
    utr_data = player.data
    high_data = player.data
    low_data = player.data
    # add_dat = player.data
    utr_graph = generate_graph(utr_data, 'utr')
    high_graph = generate_graph(high_data, 'high')
    low_graph = generate_graph(low_data, 'low')
    singles_matches = SinglesMatch.objects.filter(player1=player)
    doubles_matches = DoublesMatch.objects.filter(Q(player1=player) | Q(player2=player))
    singles=len(singles_matches)
    doubles=len(doubles_matches)
    singles_wins = len(SinglesMatch.objects.filter(Q(player1=player) & Q(win=True)))
    doubles_wins = len(DoublesMatch.objects.filter(Q(Q(player1=player) | Q(player2=player))&Q(win=True)))
    matches_played = len(singles_matches)+len(doubles_matches)

    context={'player':player,
             'singles_matches':singles_matches,
             "doubles_matches":doubles_matches,
             "doubles":doubles,
             "singles":singles,
             "singleswins":singles_wins,
             "doubleswins":doubles_wins,
             "matches_played":matches_played,
             'utr_graph': utr_graph,
            'high_graph': high_graph,
            'low_graph': low_graph,
             }
    
    return render(request,'base/profile.html',context)

    # add ing img Clinician Profile DAO 
def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("duel-form")
    context = {"page": page}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username of password does not exist")
    return render(request, "base/login_register.html", context)

@login_required(login_url="login")
def logDuel(request):
    if request.method == 'POST':
        duel_form = DuelForm(request.POST, prefix='duel')
        singles_formset = SinglesMatchInlineFormSet(request.POST, prefix='singles')
        doubles_formset = DoublesMatchInlineFormSet(request.POST, prefix='doubles')

        if duel_form.is_valid() and singles_formset.is_valid() and doubles_formset.is_valid():
            duel_instance = duel_form.save()
            singles_formset.instance = duel_instance
            singles_formset.save()
            doubles_formset.instance = duel_instance
            doubles_formset.save()
            return redirect("players") 
    else:
        duel_form = DuelForm(prefix='duel')
        singles_formset = SinglesMatchInlineFormSet(prefix='singles')
        doubles_formset = DoublesMatchInlineFormSet(prefix='doubles')

    return render(request, 'base/duel_form.html', {'duel_form': duel_form, 'singles_formset': singles_formset, 'doubles_formset': doubles_formset})

@login_required(login_url="login")
def logMatch(request):
    if request.method == 'POST':
        duel_form = DuelForm(request.POST, prefix='duel')
        singles_formset = SinglesMatchInlineForm(request.POST, prefix='singles')
        doubles_formset = DoublesMatchInlineForm(request.POST, prefix='doubles')

        if duel_form.is_valid() and singles_formset.is_valid() and doubles_formset.is_valid():
            duel_instance = duel_form.save()
            singles_formset.instance = duel_instance
            singles_formset.save()
            doubles_formset.instance = duel_instance
            doubles_formset.save()
            return redirect("players") 
    else:
        duel_form = DuelForm(prefix='duel')
        singles_formset = SinglesMatchInlineForm(prefix='singles')
        doubles_formset = DoublesMatchInlineForm(prefix='doubles')

    return render(request, 'base/match_form.html', {'duel_form': duel_form, 'singles_formset': singles_formset, 'doubles_formset': doubles_formset})

def logoutUser(request):
    logout(request)
    return redirect("home")

def duel_list(request):
    duels = Duel.objects.all()
    return render(request, 'base/teamstats.html', {'duels': duels})



def scrapingtest(request):
    login_url = 'https://app.utrsports.net/'
    username = 'Pankaj1970@gmail.com'
    password = 'Shrish@2005'
    html_content=""
    webdriver_path = "C:/Users/email/Documents/ResultTracker/bin/msedgedriver.exe"
    
    options = webdriver.EdgeOptions()
    options.use_chromium = True  # Set this to True for the Chromium-based Edge browser
    # options.add_argument("--headless")
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-notifications')

    driver = webdriver.Edge(executable_path=webdriver_path, options=options)
    driver.get(login_url)

    email_field = driver.find_element(By.ID, 'emailInput')  # Replace with the actual attribute
    password_field = driver.find_element(By.ID, 'passwordInput')  # Replace with the actual attribute
    email_field.send_keys('Pankaj1970@gmail.com')
    password_field.send_keys('Shrish@2005')
    submit_button = driver.find_element(By.XPATH, '//button[text()="SIGN IN"]')
    submit_button.click()

    other_page_url = 'https://app.utrsports.net/profiles/936660'
        
    
#     driver.get(url)
    wait_time = 3

# # Use time.sleep() to wait for the specified time
    time.sleep(wait_time)
    profile_url = 'https://app.utrsports.net/profiles/936660'
    driver.get(profile_url)

    # Wait for a while to ensure the page is loaded
    time.sleep(wait_time)
    html_content=driver.page_source
    # Find the element using XPath


    xpath_expression = '//*[@id="myutr-app-body"]/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]'
    element = driver.find_element(By.XPATH, xpath_expression)
    html_content=float(element.text)


#     max_wait_time = 100
#     element_xpath = '//*[@id="player-profile"]/section[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/h2'

#     element = driver.find_element("xpath", element_xpath)
#     html_content = element.text
#     html_content=html_content.split()
#     html_contenth=html_content[0]
#     html_contentl=html_content[2]


    
    context = {
        'data':html_content

    }
    driver.quit()

    return render(request, 'base/logistic.html',context)

# //*[@id="player-profile"]/section[2]/div[2]/div/div[2]/div[2]/div/div[1]/div
# def scraping(request):
#     url = 'https://worldtennisnumber.com/eng/player-profile?id=60a4ed8bbf0fe5a69879e586'
    
#     # Specify the path to chromedriver.exe
#     webdriver_path = "C:/Users/email/Documents/ResultTracker/bin/msedgedriver.exe"
    
#     # Create Chrome WebDriver instance
#     options = webdriver.EdgeOptions()
#     options.use_chromium = True  # Set this to True for the Chromium-based Edge browser
#     options.add_argument("--headless")
#     options.add_argument('--disable-extensions')
#     options.add_argument('--disable-notifications')

# # Initialize Microsoft Edge WebDriver with the specified msedgedriver.exe and options
#     driver = webdriver.Edge(executable_path=webdriver_path, options=options)
#     driver.get(url)
#     wait_time = 10

# # Use time.sleep() to wait for the specified time
#     time.sleep(wait_time)
#     max_wait_time = 100
#     element_xpath = '//*[@id="player-profile"]/section[1]/div/div/div[2]/div/div/div[3]'  
#     # Wait until the content of the header element changes

#     image_data = driver.find_element("xpath", element_xpath)

#     img_data = base64.b64decode(image_data)
#     img_np = np.frombuffer(img_data, dtype=np.uint8)
#     img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)    
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     largest_contour = max(contours, key=cv2.contourArea)
#     x, y, w, h = cv2.boundingRect(largest_contour)
#     roi = img[y:y+h, x:x+w]

#     context = {
#         'data': html_content
#     }
#     driver.quit()

#     return render(request, 'base/logistic.html',context)






# def scraping(url):
#     # url = 'https://worldtennisnumber.com/eng/player-profile?id=60a4ed8bbf0fe5a69879e586'

#     # Specify the path to chromedriver.exe
#     webdriver_path = "C:/Users/email/Documents/ResultTracker/bin/msedgedriver.exe"

# # Create Chrome WebDriver instance
#     options = webdriver.EdgeOptions()
#     options.use_chromium = True  # Set this to True for the Chromium-based Edge browser
#     options.add_argument("--headless")
#     options.add_argument('--disable-extensions')
#     options.add_argument('--blink-settings=imagesEnabled=false')
#     options.add_argument('--disable-notifications')

# # Initialize Microsoft Edge WebDriver with the specified msedgedriver.exe and options
#     driver = webdriver.Edge(executable_path=webdriver_path, options=options)
#     driver.get(url)
#     wait_time = 10

# # Use time.sleep() to wait for the specified time
#     time.sleep(wait_time)
#     max_wait_time = 100
#     element_xpath = '//*[@id="player-profile"]/section[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/h2'  
#     # Wait until the content of the header element changes

#     element = driver.find_element("xpath", element_xpath)
#     html_content = element.text
#     html_content=html_content.split()

#     # Access the text content of the element
# # scraped_data = element.text

    
#     driver.quit()

#     return html_content  
    

# def scrapingtest(request):
#     players=Player.objects.all()
#     for player in players:
#         ranking_data = scraping(player.url)  # Replace with your actual scraping function
#         date = datetime.date.today()
#         high=ranking_data[0]
#         low=ranking_data[2]


    
   
#         # Convert the date to a string before serializing
#         date_str = date.strftime("%Y-%m-%d")
#         # Update data attribute with the scraped ranking and date
#         # output.append({
#         #     'high': high,
#         #     'low': low,
#         #     'date': date_str,
#         # })
#         player.data.append({
#             'high': high,
#             'low': low,
#             'date': date_str,
#         })

#         player.save()
    

#     return(request,'base/logistic.html')