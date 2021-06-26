import requests
import tkinter as tk
import webbrowser as wb

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.vaccine = tk.Button(self, text="Find a COVID-19 Vaccination Center Near Me", command=self.vaccination)
        self.vaccine.pack(side="top")

        self.tests = tk.Button(self, text="Find a COVID-19 Assessment Center Near Me", command=self.testing)
        self.tests.pack(side="top")

        self.cases = tk.Button(self, text="Updated COVID-19 Case Counts", command=self.casecounts)
        self.cases.pack(side="top")

        self.rollout = tk.Button(self, text="Information on Canada's Vaccine Rollout", command=self.vacroll)
        self.rollout.pack(side="top")

        self.discord = tk.Button(self, text="Join the Vaccine Hunters Canada Discord Server!", command=self.vachunt)
        self.discord.pack(side="top")

        self.quit = tk.Button(self, text="Close the Program", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def vaccination(self):
        wb.open("https://www.google.ca/maps/search/covid+vaccine+near+me")

    def testing(self):
        wb.open("https://www.google.ca/maps/search/covid+assessment+sites+near+me")

    def casecounts(self):
        window = tk.Toplevel(self.master)
        window.title("COVID-19 Case Counts - Canada")
        
        requestAPI = requests.get("https://api.covid19tracker.ca/summary")
        api = requestAPI.json()["data"]

        tk.Label(master=window, text="As of " + api[0]["latest_date"] + " in Canada, there are: \n" + api[0]["change_cases"] + " new cases\n"
         + api[0]["change_fatalities"] + " new deaths\n"
         + api[0]["change_recoveries"] + " new recoveries").pack()
        tk.Button(master=window, text="Click here to see a visualization of cases in Canada", command=self.casecountvisual).pack()

    def casecountvisual(self):
        wb.open("https://www.google.com/search?q=covid+19+cases")

    def vacroll(self):
        wb.open("https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19/vaccines/how-vaccinated.html")

    def vachunt(self):
        wb.open("https://discord.gg/nKAE9Cta")
        

root = tk.Tk()
topFrame = tk.Frame()
tk.Label(text="Welcome to the COVID-19 Information Center \nHere, you'll find resources to help the world fight against the COVID-19 pandemic!").pack(side="top")
app = Application(master=root)
app.master.title("COVID-19 Information Center")
app.mainloop()