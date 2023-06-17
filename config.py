import os

api_id = int(os.environ.get("API_ID", "22108820"))
api_hash = os.environ.get("API_HASH", "301a39af78de73406a67c75ad7dd7301")
bot_token = os.environ.get("BOT_TOKEN", "6196461165:AAFZ0fX5-F2gMb0JNQauTJma2ljHRwyiEeU")
# =========================================================== #

db_url = os.environ.get("DB_URL", "Menfes03")
db_name = os.environ.get("DB_NAME", "mongodb+srv://Menfes03:fadhil12345@cluster0.psjzpkc.mongodb.net/?retryWrites=true&w=majority")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001509543098"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001956779347"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001964399865"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "5799212681"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "15"))
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

hastag = os.environ.get("HASTAG", "#fwbcantik #fwbganteng #fwbgalau #fwbrandom #fwbpap #fwbkepo").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/ab262a6eed7b5e4879ae3.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/f189097501089f5cc38dd.jpg")
pic_talent = os.environ.get("PIC_TALENT", "https://telegra.ph//file/30c3b445e0c33c90cb0b6.jpg")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "0")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "0")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat FWB😉\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya FWB👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} hallo selamat datang dibot auto post FWB base✨\n\nIni adalah bot Menfes ya FWB, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#fwbrandom Untuk Random\n#fwbkepo untuk Bertanya\n#fwbgalau untuk Berbagi Cerita\n#fwbpap untuk ngirim pap kecuali pap kemaluan\n\nContoh:\n {mention} Cari Mutualan Dom Depok #fwbganteng/n Contact @chloppii")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#fwbcantik Untuk Cewek
#fwbganteng Untuk Cowok
#fwbgalau Untuk Curhat
#fwbrandom Untuk Random
#fwbkepo Bertanya
#fwbpap untuk pap rate kecuali pap kemaluan

""")
