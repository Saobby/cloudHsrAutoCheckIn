import os

cookies = os.getenv("mihoyo_cookies")
cookies_ = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
device_fp = cookies_["DEVICEFP"]
device_id = cookies_["_MHYUUID"]
channel_id = 1
app_id = 8
app_key = "4650f3a396d34d576c3d65df26415394"
game_biz = "hkrpg_cn"
weblogin_url = "https://hkrpg-sdk.mihoyo.com/hkrpg_cn/combo/granter/login/webLogin"
weblogin_headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9", "Content-Type": "application/json", "Cookie": cookies,
                    "Host": "hkrpg-sdk.mihoyo.com", "Origin": "https://sr.mihoyo.com", "Referer": "https://sr.mihoyo.com/",
                    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                    "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": '"Windows"', "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/120.0.0.0 Safari/537.36",
                    "X-Rpc-Channel_id": str(channel_id), "X-Rpc-Client_type": "22", "X-Rpc-Device_fp": device_fp,
                    "X-Rpc-Device_id": device_id, "X-Rpc-Device_model": "Chrome%20120.0.0.0",
                    "X-Rpc-Device_name": "Chrome", "X-Rpc-Device_os": "Windows%2010%2064-bit",
                    "X-Rpc-Game_biz": game_biz, "X-Rpc-Language": "zh-cn", "X-Rpc-Mdk_version": "2.19.5"}

login_url = "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/gamer/api/login"
get_notification_url = "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/gamer/api/listNotifications?status=NotificationStatusUnread&type=NotificationTypePopup&is_sort=true"
get_wallet_url = "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/wallet/wallet/get"
read_notification_url = "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/gamer/api/ackNotification"
login_headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br",
                 "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "keep-alive", "Cookie": cookies,
                 "Host": "cg-hkrpg-api.mihoyo.com", "Origin": "https://sr.mihoyo.com",
                 "Referer": "https://sr.mihoyo.com/",
                 "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                 "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": '"Windows"', "Sec-Fetch-Dest": "empty",
                 "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/120.0.0.0 Safari/537.36",
                 "X-Rpc-App_id": "", "X-Rpc-Cg_game_biz": game_biz,
                 "X-Rpc-Channel": "mihoyo", "X-Rpc-Client_type": "16", "X-Rpc-Cps": "pc_mys",
                 "X-Rpc-Device_id": device_id, "X-Rpc-Device_model": "Unknown", "X-Rpc-Device_name": "Unknown",
                 "X-Rpc-Language": "zh-cn", "X-Rpc-Op_biz": "clgm_hkrpg-cn", "X-Rpc-Sys_version": "Windows 10",
                 "X-Rpc-Vendor_id": "2"}

get_version_url = "https://sdk-static.mihoyo.com/combo/box/api/config/cloud_rpg/cloud_config?cloud_config=config"
get_config_headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br",
                      "Accept-Language": "zh-CN,zh;q=0.9", "Origin": "https://sr.mihoyo.com",
                      "Referer": "https://sr.mihoyo.com/",
                      "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                      "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": '"Windows"', "Sec-Fetch-Dest": "empty",
                      "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/120.0.0.0 Safari/537.36"}


if __name__ == "__main__":
    print(cookies_)
