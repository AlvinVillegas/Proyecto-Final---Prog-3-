from selenium.webdriver.common.by import By
from pytest import mark
import time
from datetime import datetime
from selenium import webdriver

def guardarFoto(driver, donde):
    diferente = datetime.now().strftime("%H-%M-%S")
    driver.save_screenshot('./img/'+donde+ 'foto'+diferente+'.png')

def login():
    driver = webdriver.Chrome()
    driver.get("https://rise.classiccompiler.com/index.php/signin")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="signin-form"]/button').click()
    return driver

@mark.parametrize("usu,contra", [("admin@demo.com", "riseDemo"), ("fail", "fail")])
def testing_login(usu,contra):
    driver = webdriver.Chrome()
    driver.get("https://rise.classiccompiler.com/index.php/signin")
    driver.find_element(By.ID, 'email').clear()
    driver.find_element(By.ID, 'password').clear()
    driver.find_element(By.ID, 'email').send_keys(usu)
    driver.find_element(By.ID, 'password').send_keys(contra)
    driver.find_element(By.XPATH, '//*[@id="signin-form"]/button').click()
    guardarFoto(driver, 'login')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/dashboard'

def testing_userName():
    driver = login();
    user = driver.find_element(By.XPATH, '//*[@id="user-dropdown"]/span[2]').text
    guardarFoto(driver, 'username')
    assert user == 'John Doe'

def testing_mail():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[2]/a').click()
    guardarFoto(driver, 'mail')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/mailbox'

def testing_clients():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[3]/a').click()
    guardarFoto(driver, 'clientes')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/clients'

def testing_leads():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a').click()
    guardarFoto(driver, 'leads')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/leads'

def testing_projects():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[5]/a').click()
    guardarFoto(driver, 'projects')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/projects/all_projects'

def testing_tasks():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[6]/a').click()
    guardarFoto(driver, 'task')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/projects/all_tasks'

def testing_invoices():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[7]').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[7]/ul/li/a').click()
    guardarFoto(driver, 'invoices')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/invoices'

def testing_teamMembers():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[8]/a').click()
    guardarFoto(driver, 'team')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/team_members'

def testing_incomevsexpenses():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[9]/a').click()
    guardarFoto(driver, 'expenses')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/expenses/income_vs_expenses'

def testing_settings():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[11]/a').click()
    guardarFoto(driver, 'settings')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/settings/general'

def testing_changeLanguage():
    driver = login()
    oldText = driver.find_element(By.XPATH, '//*[@id="page-content"]/div[3]/div[3]/div/div[1]').text
    driver.find_element(By.XPATH, '//*[@id="default-navbar"]/div/div/div/ul/li[4]').click()
    driver.find_element(By.XPATH, '//*[@id="default-navbar"]/div/div/div/ul/li[4]/ul/li/a[6]').click()
    time.sleep(4)
    newText = driver.find_element(By.XPATH, '//*[@id="page-content"]/div[3]/div[3]/div/div[1]').text
    guardarFoto(driver, 'changelanguage')
    assert oldText != newText

def testing_ayuda():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]/ul/li[1]/a').click()
    guardarFoto(driver, 'ayuda')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/help'


def testing_articulosAyuda():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]/ul/li[2]/a').click()
    guardarFoto(driver, 'articuloayuda')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/help/help_articles'


def testing_categoriasDeAyuda():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]/ul/li[3]/a').click()
    guardarFoto(driver, 'categoriaayuda')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/help/help_categories'


def testing_baseDeConocimiento():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]/ul/li[4]/a').click()
    guardarFoto(driver, 'baseconocimiento')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/knowledge_base'


def testing_articulosBC():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]/ul/li[5]/a').click()
    guardarFoto(driver, 'articulosbc')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/help/knowledge_base_articles'


def testing_categoriasBC():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]').click()
    driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[10]/ul/li[6]/a').click()
    guardarFoto(driver, 'categoriasbc')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/help/knowledge_base_categories'


def testing_MiPerfil():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="default-navbar"]/div/div/div/ul/li[8]').click()
    driver.find_element(By.XPATH, '//*[@id="default-navbar"]/div/div/div/ul/li[8]/ul/li[1]/a').click()
    guardarFoto(driver, 'miperfil')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/team_members/view/1/general'


def testing_CambiarContra():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="default-navbar"]/div/div/div/ul/li[8]').click()
    driver.find_element(By.XPATH, '//*[@id="default-navbar"]/div/div/div/ul/li[8]/ul/li[1]/a').click()
    guardarFoto(driver, 'cambiarcontra')
    assert driver.current_url == 'https://rise.classiccompiler.com/index.php/team_members/view/1/account'

