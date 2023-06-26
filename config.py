import os

api_id = int(os.environ.get("API_ID", "12857763"))
api_hash = os.environ.get("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d")
bot_token = os.environ.get("BOT_TOKEN", "6213624396:AAFVscQg0PgmXdX7AcCh8jgWj5DI9kdB8js")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://AnakRp:fadhil123@cluster0.p7yaf7z.mongodb.net/")
db_name = os.environ.get("DB_NAME", "AnakRp")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001892588505"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001624974363"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001949406995"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6129133916"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "20"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "100"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "500"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "500"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "500"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "500"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "500"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "500"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#FwbGirl #FwbBoy #FwbAsk #FwbStory #FwbSpill #FwbFind").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/19ec604009233e6d8997d.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/705e40a31eaf5d5ff4260.jpg")
pic_talent = os.environ.get("PIC_TALENT", "https://telegra.ph//file/5745935c975255c34a06a.jpg")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "0")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "0")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat FWB😉\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya FWB👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} hallo selamat datang dibot auto post FWB base✨\n\nIni adalah bot Menfes ya FWB, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#FwbGirl Untuk Cewek\n#FwbBoy Untuk Cowok\n#FwbAsk Untuk Bertanya\n#FwbStory Untuk Cerita\n#FwbSpill Untuk Spill\n#FwbFind untuk Mencari Pasangan\n\nContoh:\n {mention} Cari Mutualan Dom Depok #FwbGirl/n Contact @OWNERMIKU")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#FwbGirl Untuk Cewek
#FwbBoy Untuk Cowok
#FwbAsk Untuk Bertanya
#FwbStory Untuk Cerita
#FwbSpill Untuk Spill
#FwbFind untuk Mencari Pasangan

""")
