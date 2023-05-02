import os

api_id = int(os.environ.get("API_ID", "11496628"))
api_hash = os.environ.get("API_HASH", "3dfd4ab14279d43dee1f5fd1051ce406")
bot_token = os.environ.get("BOT_TOKEN", "6290482856:AAGqNk8RygkY1qh32TsHH-govZIsiKt7ObM")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Menfes:menfes123@menfes.42w3efm.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "Menfes")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001894348982"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001542869898"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001794397555"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1998691839"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "6"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "100"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "5000"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "5000"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "5000"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "5000"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "5000"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "5000"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#strboy #strgirl #strcurhat #strrandom #strrandom #strrate #strask").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/photo-05-02-3")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/strtalent-05-02")
pic_talent = os.environ.get("PIC_TALENT", "https://telegra.ph/strtalent-05-02")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "0")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "0")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat STR😉\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess ya STR👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} Sobat Efbees✨\n\nIni adalah bot Menfes ya STR, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#strboy / #strgirl untuk Mencari Pasangan, Teman , Partner dll\n#strask untuk Bertanya\n#strcurhat untuk Berbagi Cerita\n#strpap untuk ngirim pap kecuali pap kemaluan\n\nContoh:\n {mention} Cari Mutualan Dom Depok #strgril/n Contact @onefled")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#strgirl Untuk Cewek
#strboy Untuk Cowok
#strcurhat Untuk Curhat
#strrandom Untuk Random
#strask Bertanya
#strpap untuk pap rate kecuali pap kemaluan

""")
