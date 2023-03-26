запити на імпорт 
від bs4 імпорт BeautifulSoup

URL = "https://www.olx.ua/d/uk/obyavlenie/prodam-banan-kievskiy-super-karlik-IDC7KUN.html"
дані = запити. отримати (URL). Текст

суп = BeautifulSoup(дані, особливості="html.parser")

product_name = суп. find_all("h1", {"class":"css-1soizd2 er34gjf0"})
product_price = суп. find_all("h3", {"class":"css-ddweki er34gjf0"})
product_description = суп. find_all("div", {"class":"css-bgzo2k er34gjf0"})
Similar_ads = суп. find_all("div", {"class":"css-1wbpwse"})
print("Назва продукта -", product_name)
print("Ціна продукта -", product_price)
print("Опис продукта -", product_description)
print("Схожі товари -", Similar_ads)