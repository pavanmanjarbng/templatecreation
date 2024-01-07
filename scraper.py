from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
from datetime import datetime
def scrape_webinar_details(webinar_URL, webinar_date, webinar_speaker):
    url = urlopen(webinar_URL).read()
    soup = BeautifulSoup(url, features='html.parser')
    currentDay = datetime.now().day
    currentMonth = datetime.now().strftime('%h')

    creation_date = str(currentMonth) + str(currentDay)
    creation_date = creation_date.upper()
    # Scraping logic (as per your provided code)
    webinar_title = soup.find_all('h1')[0].get_text()
    # ... (other scraping logic)
    webinar_speaker_fname = webinar_speaker.split(" ")[0:][0]
    webinar_speaker_lname = webinar_speaker.split(" ")[1:][0]
    webinar_speaker_shortname = webinar_speaker_fname+"_"+webinar_speaker_lname
    webinar_speaker_shortname = webinar_speaker_shortname.upper()

    webinar_URL_final = webinar_URL+"?channel=mailer&camp=webinar&AdGroup="+webinar_speaker_shortname+"_"+webinar_date+"_"+creation_date+"_SF"

    web_date = soup.find_all('div', attrs={'class': 'webinatr-date'})[0].find_all('div', attrs={'class': 'date-items'})[0].find_all('div')[0].get_text()
    webinar_duration = soup.find_all('div', attrs={'class': 'webinatr-date'})[0].find_all('div', attrs={'class': 'date-items'})[2].find_all('div')[0].get_text()
    webinar_time = soup.find_all('div', attrs={'class': 'webinatr-date'})[0].find_all('div', attrs={'class': 'date-items'})[1].find_all('div')[0].get_text()

    webinar_overview = soup.find_all('div', attrs={'class': 'webinar-contents'})[0].find_all('p')[0].get_text()
    webinar_overview_2 = soup.find_all('div', attrs={'class': 'webinar-contents'})[0].find_all('p')[0].next_sibling.get_text()
    webinar_overview_f = webinar_overview+ " "+webinar_overview_2
    webinar_overview_f = webinar_overview_f.split(".")

    webinar_overview_f = webinar_overview_f[0]+ ". "

    fullstring = webinar_overview
    substring = "The use of this seal confirms"

    if substring in fullstring:
        webinar_overview = soup.find_all('div', attrs={'class': 'webinar-contents'})[0].find_all('p')[1].get_text()
        webinar_overview_f = webinar_overview

    url_speaker = soup.find_all('img')[1]
    url_speaker = url_speaker['src']
    url_speaker = url_speaker.split("/")[3:][0]

    url_speaker_final = "https://hrtrainonline.com/control/speakerprofile?speaker_id="+url_speaker

    url2 = urlopen(url_speaker_final).read()
    soup2 = BeautifulSoup(url2, features='html.parser')

    speaker_title = soup2.find_all('h4')[0].next_sibling

    if webinar_speaker == "Ronald Adler":
        speaker_overview = "is the president-CEO of Laurdan Associates, Inc, a veteran owned, human resource management consulting firm specializing in HR audits, employment practices liability risk management, HR metrics and benchmarking, strategic HR-business issues and unemployment insurance."
    elif webinar_speaker == "Dorothy Neddermeyer":
        speaker_overview = "is a successful influencer in the public and private sectors. As a consultant, coach, and keynote speaker, she brings 30-plus years of global experience to leadership development, behavioral change, and human potential."
    elif webinar_speaker == "Mandi Stanley":
        speaker_overview = "With more than 16 years of experience on the seminar circuit, Certified Speaking Professional Mandi Stanley works primarily with business leaders who want to boost their professional image and with people who want to be better speakers and writers."
    elif webinar_speaker == "David Wudyka":
        speaker_overview = ", MBA, is the Managing Principal of Westminster Associates of Wrentham, MA. He has over thirty years experience as a Human Resource Consultant with a specialty in Compensation Consulting."
    elif webinar_speaker == "Kathryn Dager":
        speaker_overview = ", MA, President and Founder of Profitivity Inc. in 1985, is an internationally recognized Speaker, Consultant, and Trainer for small and large organizations in all industries, worldwide. With over 36 years of business consulting, talent empowerment, and leadership and management development, she has helped hundreds of business leaders and their teams structure their business for cultural agility, higher performance, sustained profitability, and growth."
    elif webinar_speaker == "Lynn Ware":
        speaker_overview = "PhD , President and CEO As CEO of Integral Talent Systems, Inc. (ITS) based in Silicon Valley, California, Dr Ware is an Industrial/Organizational Psychologist who has practiced for over 25 years in the talent management field with a strong focus on how to increase employee productivity for the benefit of achieving business goals."
    elif webinar_speaker == "Mike Thomas":
        speaker_overview = "has worked in the IT training business since 1989, He is a subject matter expert in a range of technologies including Microsoft Office and Apple Mac, In 2012 He founded theexceltrainer where he has produced nearly 200 written and video-based Excel tutorials."
    elif webinar_speaker == "David Wudyka":
        speaker_overview = ", MBA, is the Managing Principal of Westminster Associates of Wrentham, MA. He has over thirty years experience as a Human Resource Consultant with a specialty in Compensation Consulting. David has taught extensively in colleges and universities such as UMass Boston, Bryant University, and the US Coast Guard Academy."
    elif webinar_speaker == "Brenda Neckvatal":
        speaker_overview = "is an international award-winning HR professional and two time Best Selling Author. Not only does she help business leaders get the people side of their business right, she is a specialist in crisis management, government contracting HR compliance, and mentor to rising entrepreneurs, business leaders, HR champions and professionals."
    elif webinar_speaker == "Karla Brandau":
        speaker_overview = "is a thought leader in management and team building techniques. She trains managers to improve their relationship with the employees to earn their gift of discretionary effort."
    elif webinar_speaker == "Maure Metzger":
        speaker_overview = ", EDD, is an author, trainer, consultant and psychologist. Her 20+ years of experience as a consultant, trainer and psychologist provides for a unique and holistic approach to her work with organizations and employees."
    elif webinar_speaker == "David Cohen":
        speaker_overview = ", EdD is a seasoned management consultant passionate about building organizations through the successful alignment of their people to the corporate values and corresponding behaviors. He works with organizations and their leaders to ensure the clear articulation of the culture and the application of that knowledge to building integrated talent management processes and practices and improving employee engagement."
    elif webinar_speaker == "Glynis Devine":
        speaker_overview = "is a Currency-Driven Performance expert specializing in developing women leaders. SPOILER ALERT: THIS Currency* has nothing to do with money!"
    elif webinar_speaker == "Thea Ducrow":
        speaker_overview = "PhD, your mentor in the quest of integrating AI into your HR practices. As an AI Creative Leadership Consultant, she acknowledges the complexities HR professionals confront in this swiftly evolving, technology-driven era. Amid these growing challenges, Dr. Ducrow emerges as your reliable advisor who has navigated this landscape and effectively harnessed the power of AI in human resources."
    else:
        speaker_overview = soup2.find_all('b')[0].next_sibling

    speaker_overview = speaker_overview.split(".")
    speaker_overview = speaker_overview[0]+ ". "+speaker_overview[1]+". "


    base = os.path.dirname(os.path.abspath(__file__))
    html = open(os.path.join(base, 'HRTO_New.html'), encoding="utf8")
    soup3 = BeautifulSoup(html, 'html.parser')

    soup3.title.string = webinar_title
    soup3.find_all('td', attrs={'alt': 'title'})[0].string = webinar_title
    soup3.find_all('p', attrs={'alt': 'web-date'})[0].string = web_date
    soup3.find_all('p', attrs={'alt': 'web-time'})[0].string = webinar_time
    soup3.find_all('p', attrs={'alt': 'web-duration'})[0].string = webinar_duration

    reg_url = soup3.find_all('a', attrs={'alt': 'link1'})[0]
    reg_url['href'] = webinar_URL_final

    soup3.find_all('td', attrs={'alt': 'overview'})[0].string = webinar_overview_f

    new_tag = soup.new_tag("strong")
    new_tag.string = "Overview: "
    original_tag = soup3.find_all('td', attrs={'alt': 'overview'})[0]

    original_tag.insert(0,new_tag)

    new_tag2 = soup3.new_tag("br")
    original_tag2 = soup3.find_all('td', attrs={'alt': 'overview'})[0]
    original_tag2.insert(1,new_tag2)

    new_tag3 = soup.new_tag("a", href=webinar_URL_final)
    new_tag3['style'] = 'color: #46b007; text-decoration: none;'

    original_tag3 = soup3.find_all('td', attrs={'alt': 'overview'})[0]

    original_tag3.append(new_tag3)
    new_tag3.string = " Read More.."

    new_tag4 = soup.new_tag("br")
    original_tag4 = soup3.find_all('td', attrs={'alt': 'overview'})[0]
    original_tag4.append(new_tag4)

    new_tag5 = soup.new_tag("strong")
    new_tag5.string = "Speaker: "
    original_tag5 = soup3.find_all('td', attrs={'alt': 'overview'})[0]
    original_tag5.append(new_tag5)

    new_tag6 = soup.new_tag("br")
    original_tag6 = soup3.find_all('td', attrs={'alt': 'overview'})[0]
    original_tag6.append(new_tag6)

    new_tag7 = soup.new_tag("strong")
    new_tag7.string = webinar_speaker
    original_tag7 = soup3.find_all('td', attrs={'alt': 'overview'})[0]
    original_tag7.append(new_tag7)

    original_tag8 = soup3.find_all('td', attrs={'alt': 'overview'})[0]
    original_tag8.append(speaker_overview)

    new_tag9 = soup.new_tag("a", href=url_speaker_final)
    new_tag9['style'] = 'color: #46b007; text-decoration: none;'

    original_tag9 = soup3.find_all('td', attrs={'alt': 'overview'})[0]

    original_tag9.append(new_tag9)
    new_tag9.string = " Read More.."

    folder_path = 'created/'  # Replace with your desired folder path

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the file name
    file_name = "webinar_mailer_" + webinar_date + "_" + webinar_speaker_shortname +"_"+creation_date+".html"

    # Combine the folder path and file name to get the complete file path
    edited_file = os.path.join(folder_path, file_name)

    # Write the content to the file
    with open(edited_file, "w", encoding="utf-8") as f_output:
        f_output.write(soup3.prettify())

    # Constructing the final dictionary
    scraped_data = {
        "webinar_title": webinar_title,
        "webinar_date": web_date,  # Assuming 'web_date' is obtained in your scraping logic
        "webinar_time": webinar_time,  # Assuming 'webinar_time' is obtained in your scraping logic
        "webinar_duration": webinar_duration,  # Assuming 'webinar_duration' is obtained in your scraping logic
        "webinar_overview": webinar_overview_f,  # Assuming 'webinar_overview_f' is obtained in your scraping logic
        "speaker_overview": speaker_overview,  # Assuming 'speaker_overview' is obtained in your scraping logic
        "webinar_URL_final": webinar_URL_final,  # Assuming 'webinar_URL_final' is obtained in your scraping logic
        "url_speaker_final": url_speaker_final  # Assuming 'url_speaker_final' is obtained in your scraping logic
    }

    return scraped_data, file_name
