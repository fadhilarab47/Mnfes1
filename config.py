import os

api_id = int(os.environ.get("API_ID", "12857763"))
api_hash = os.environ.get("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d")
bot_token = os.environ.get("BOT_TOKEN", "5818056238:AAGpnZ2X5RleSv5b8NBQSAZyAnUGc_iAp4Y")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://fadhil:fadhil123@cluster0.jvnx5r6.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "fadhil")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001809708760"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001537697834"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001554653997"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1345594412"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "1"))
batas_talent = int(os.environ.get("BATAS_TALENT", "15"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#FbsGirl #FbsBoy #FbsAsk #FbsFind #FbsSpill #FbsStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/0d5a174c3dd2a156d02e8.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/a26cef38c65c132d555a5.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat Mengirim, Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya Efbees")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱\n\nIni adalah bot menfess ya Efbees, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. Sesuai rules ya efbees")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#FbsBoy / #FbsGirl untuk Mencari Pasangan, Teman , Partner dll
#FbsAsk untuk Bertanya
#FbsStory untuk Berbagi Cerita
#FbsSpill untuk Spill Masalah
#FbsFind untuk Mencari Pasangan, Teman, Partner dll
""")
