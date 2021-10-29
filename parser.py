from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox



def check_crypto_price():
    root = Tk()

    root['bg'] = '#fafafa'
    root.title('Convert Crypto to Currency')
    root.geometry('600x250')

    lbl = Label(root, text="Выбери крипту")
    lbl.place(relx=0.02, rely=0.15)
    lbl2 = Label(root, text="Выбери валюту")
    lbl2.place(relx=0.45, rely=0.15)
    lbl3 = Label(root, text="Кол-во крипты")
    lbl3.place(relx=0.02, rely=0.3)

    combo = Combobox(root)
    combo['values'] = ['RUB', 'USD', 'EUR']
    combo.current(1)
    combo.place(relx=0.62, rely=0.15)

    combo2 = Combobox(root)
    combo2['values'] = ['DERC', 'BTC', 'BNB', 'ETH', 'BUSD', 'USDT', 'SOL']
    combo2.current(1)
    combo2.place(relx=0.19, rely=0.15)

    txt = Entry(root, width=10)
    txt.place(relx=0.2, rely=0.305)

    def after_button():

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '5000',
            'convert': combo.get()
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'https://coinmarketcap.com/api',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            for i in data['data']:
                if i['symbol'] == combo2.get():
                    lbl4 = Label(root, text=f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{txt.get()} {i['name']} in {combo.get()} is {round(float(i['quote'][combo.get()]['price']) * int(txt.get()), 2)}", font=("Arial Bold", 20))
                    lbl4.place(relx=0.2, rely=0.5)
                    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    print(f"{txt.get()} {i['name']} in {combo.get()} is {round(float(i['quote'][combo.get()]['price']) * int(txt.get()), 2)}")
                    return f"{txt.get()} {i['name']} in {combo.get()} is {round(float(i['quote'][combo.get()]['price']) * int(txt.get()), 2)}"
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

    btn = Button(root, text=f'Convert', command=after_button)
    btn.place(relx=0.35, rely=0.288)

    root.mainloop()
    return f'Well done!'


if __name__ == '__main__':
    print(check_crypto_price())
