#!/usr/bin/env python

from selenium import webdriver
import pickle
import time
import argparse
import os
from pathlib import Path

def get_question(driver):
    out = ""
    list = driver.find_elements_by_xpath("//form[@name='answerform']/div/div/div/div")
    for x in list[:-1]:
        out = out + x.text
    return out

def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=%s" % os.path.join(os.path.dirname(os.path.realpath(__file__)), "selenium"))
    driver = webdriver.Chrome(chrome_options=options)
    link = "https://www.khanacademy.org/login"
    driver.get(link)
    

def main(link):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=%s" % os.path.join(os.path.dirname(os.path.realpath(__file__)), "selenium"))
    driver = webdriver.Chrome(chrome_options=options)

    answer_dict = {}

    while True:
        driver.get(link)
        time.sleep(10)
        try:
            driver.find_element_by_xpath("//button[@data-test-id='letsgo-button']").click()
        except:
            pass
        time.sleep(3)
        try:

            while True:
                question = get_question(driver)
                #if question in answer_dict and "all" not in driver.find_element_by_xpath("//div[@class='instructions _125m8j1']"):
                if question in answer_dict:
                    print("knows answer")
                    #answer is known

                    for n in range(10):
                        #"//div[@class='checkbox-and-option _tqugjn']//span[@class='perseus-radio-option-content perseus-interactive']"
                        if driver.find_elements_by_xpath("//span[@class='perseus-radio-option-content perseus-interactive']")[n].text == answer_dict[question]:
                            driver.find_elements_by_xpath("//span[@class='perseus-radio-option-content perseus-interactive']")[n].click()
                            driver.find_element_by_xpath("//button[@data-test-id='exercise-check-answer']").click()
                            driver.find_element_by_xpath("//button[@data-test-id='exercise-next-question']").click()
                            break
                else:
                    text = ""
                    for n in range(10):
                            # guess a random answer
                            text = driver.find_elements_by_xpath("//span[@class='perseus-radio-option-content perseus-interactive']")[n].text
                            driver.find_elements_by_xpath("//span[@class='perseus-radio-option-content perseus-interactive']")[n].click()
                            driver.find_element_by_xpath("//button[@data-test-id='exercise-check-answer']").click()

                            #continues if guessed it wrong
                            try:
                                driver.find_element_by_xpath("//button[@data-test-id='exercise-check-answer']").click()
                            except Exception as e:
                                # happens if guessed it right
                                answer_dict[get_question(driver)] = text
                                driver.find_element_by_xpath("//button[@data-test-id='exercise-next-question']").click()
                                # continue to next question
                                break
        except Exception as e:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Khan bot')
    parser.add_argument('URL', metavar='URL', type=str, nargs="?", help='URL of problem set', default="https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-new/ab-1-3/e/one-sided-limits-from-graphs?modal=1")
    parser.add_argument('--setup', default=False, type=bool, help='Use this parameter for first-time setup')
    args = parser.parse_args()

    if args.setup:
        setup()
    else:
        main(args.URL)
