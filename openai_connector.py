
import os
import openai
import config

class OpenAIInterface:
    
    def __init__(self):
        self.key_ = "" #  <-- Enter OpenAI API key within quotes.  
        self.engine_ = "text-davinci-003"
        self.translate_prompt_ = "Translate this into English from Turkish:\n\n"
        self.news_prompt_ = "Categorize this news into one of the following categories: [Breaking news, Business news, Entertainment news, Sports news, Political news, Weather news, Science and technology news, Health news, Human interest news, Crime news, Education news, Environmental news, International news, Local news, National news, Regional news, Weather news, World news , Religional news , Other news]\n\n"
        self.temperature_ = 0.3
        self.max_tokens_ = 64
        self.top_p_ = 1
        self.frequency_penalty_ = 0.0
        self.presence_penalty_ = 0.0
    
    def translate(self, text):
        openai.api_key = self.key_
        prompt = self.translate_prompt_ + text + "\n\n"
        response = openai.Completion.create(
            engine=self.engine_,
            prompt=prompt,
            temperature=self.temperature_,
            max_tokens=self.max_tokens_,
            top_p=self.top_p_,
            frequency_penalty=self.frequency_penalty_,
            presence_penalty=self.presence_penalty_)
        translated_text = response["choices"][0]["text"]
        return translated_text
    
    def categorize(self,text):
        openai.api_key = self.key_
        prompt = self.news_prompt_ + text + "\n\n"
        response = openai.Completion.create(
            engine=self.engine_,
            prompt=prompt,
            temperature=self.temperature_,
            max_tokens=self.max_tokens_,
            top_p=self.top_p_,
            frequency_penalty=self.frequency_penalty_,
            presence_penalty=self.presence_penalty_)
        translated_text = response["choices"][0]["text"]
        return translated_text
    
#Answer: International news
text = "Uzaylılar dünyaya bir saldırı başlattı. Rusya hava kuvvetleri ivedilikle cevap verirken, Hindistan kuvvetleri barış müzakerelerine başlama kararı aldı."

#Answer: Regional news
text2 = "Türkiye'de 3.5 büyüklüğünde deprem meydana geldi. Depremde 3 kişi hayatını kaybetti, 100 kişi yaralandı. İçişleri Bakanı Süleyman Soylu, Depremde hayatını kaybeden vatandaşlarımıza Allah'tan rahmet, yaralı vatandaşlarımıza acil şifalar diliyorum. Depremde hasar gören vatandaşlarımıza da acil kurtarma çalışmalarımız devam ediyor. Depremde hasar gören vatandaşlarımızın yanında olmaya devam edeceğiz dedi."

#Answer: Sports news
text3 = "Fenerbahçe ve Galatasaray arasındaki derbiyi Fenerbahçe 3-0 kazandı."

#Answer: Business news
text4 = "Dini bayram dolayısıyla kurban fiyatlarında artış gerçekleşti."

#Answer: Religional news
text5 = "Hz. Muhammed'in dünyaya yeniden geldiği gözlemlendi."

interface = OpenAIInterface()
translated_text = interface.translate(text5)
news_category = interface.categorize(translated_text)
print(news_category)
