import os

api_id = int(os.environ.get("API_ID", "15890589"))
api_hash = os.environ.get("API_HASH", "27fe60ebafe8a74117bfae10407925c7")
bot_token = os.environ.get("BOT_TOKEN", "6826195273:AAFjSeGQGm87MdjGxBGFBbbkCoBm3STIGtg")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://doadmin:31pS5AO2y6v07G9D@db-mongodb-sgp1-13992-4042e3fd.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-13992")
db_name = os.environ.get("DB_NAME", "doadmin")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002100850265"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001537697834"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1002005957935"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002130415408"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1948147616"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "20"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "30"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "200"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "200"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "200"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "200"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "200"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "200"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#BgGirl #BgBoy #BgCurhat #BgSpill #BgPap").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/3fc66f7a03da667e94b87.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/0856d6858d9117fbdff65.jpg")
pic_talent = os.environ.get("PIC_TALENT", "https://telegra.ph//file/31aa5b2804691ec04ed9c.jpg")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "https://telegra.ph//file/8de768f664063f1bb520e.jpg")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "https://telegra.ph//file/983e3138a5883645497d3.jpg")
pic_sugar_daddy = os.environ.get("PIC_SUGAR_DADDY", "https://telegra.ph//file/df87a56dfa94043c51572.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat BG Menfes [😉](https://telegra.ph//file/5ec20cb31185ce5c7c12b.jpg)\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya BG Menfes👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} hallo selamat datang dibot auto post BG Menfes base [✨](https://telegra.ph//file/5ec20cb31185ce5c7c12b.jpg) .\n\nIni adalah bot Menfes ya BG Menfes, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#BgGirl Untuk Cewek\n#BgBoy Untuk Cowok\n#BgCurhat Untuk Curhat\n#BgPap Untuk Mengirim Pap random kalian\n\nContoh:\n. {mention} Cari Mutualan Dom Depok #BgGirl\n\nSupport: @BGMenfes_update")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
Halo {mention} [👋🏻](https://telegra.ph//file/5ec20cb31185ce5c7c12b.jpg) 

pesan mu gagal terkirim silahkan gunakan hastag:
#BgGirl / #BgBoy Untuk Mencari Pasangan, Teman , Partner FWB
#BgAsk Untuk Bertanya
#BgCurhat Untuk Berbagi Cerita / Curhat.
#BgSpill Untuk Spill Masalah / Pengalaman
#BgPap Untuk Mengirim Pap random kalian.

""")
