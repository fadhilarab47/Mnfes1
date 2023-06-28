import os

api_id = int(os.environ.get("API_ID", "21432530"))
api_hash = os.environ.get("API_HASH", "7108c3b533ab7f1756c70a95a59790f9")
bot_token = os.environ.get("BOT_TOKEN", "5715747322:AAE3UYscWsd0BJ_6Hv9zcHxCjJzXl4O_Lz0")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://fadhilubot:fadhil123@cluster0.dxhbmhf.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "fadhilubot")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001830268921"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001911983930"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001959577065"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6036408604"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "20"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "50"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "500"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "500"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "500"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "500"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "500"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "500"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#MikuGirl #MikuBoy #MikuAsk #MikuStory #MikuSpill #MikuFind").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/a6896b2fb8d013b7832e3.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/a3ad21e5abdeb32deddcf.jpg")
pic_talent = os.environ.get("PIC_TALENT", "https://telegra.ph//file/31aa5b2804691ec04ed9c.jpg")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "https://telegra.ph//file/8de768f664063f1bb520e.jpg")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "https://telegra.ph//file/983e3138a5883645497d3.jpg")
pic_sugar_daddy = os.environ.get("PIC_SUGAR_DADDY", "https://telegra.ph//file/df87a56dfa94043c51572.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat Miku😉\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya Miku👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} hallo selamat datang dibot auto post Miku base✨\n\nIni adalah bot Menfes ya FWB, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#MikuGirl Untuk Cewek\n#MikuBoy Untuk Cowok\n#MikuAsk Untuk Bertanya\n#MikuStory Untuk Cerita\n#MikuSpill Untuk Spill\n#MikuFind untuk Mencari Pasangan\n\nContoh:\n{mention} Cari Mutualan Dom Depok #MikuGirl\n\nContact @Mikuchaaann")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#MikuBoy / #MikuGirl Untuk Mencari Pasangan, Teman , Partner FWB
#MikuAsk Untuk Bertanya
#MikuStory Untuk Berbagi Cerita
#MikuSpill Untuk Spill Masalah
#MikuFind Untuk Mencari Pasangan, Teman, Partner FWB.

""")
