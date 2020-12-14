# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 淘宝秒杀脚本，扫码登录版
# from idlelib import browser
# import webbrowser
from selenium import webdriver
import datetime
import time
import sys


class MiaoSha:
    def buy(self, times, choose, browser=None):
        # 点击购物车里全选按钮
        if choose == 2:
            print("请手动勾选需要购买的商品")
            time.sleep(2)
        elif choose == 1:
            print('choose == 1')
            try:
                print('looking for //*[@id="J_SelectAll1"]/div/label')
                if browser.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label'):
                    print('//*[@id="J_SelectAll1"]/div/label')
                    browser.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label').click()
            except:
                print("找不到全选按钮")

        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            # 对比时间，时间到的话就点击结算
            if now >= times:
                print('时间到了。。。。。')

                # 点击结算按钮
                try:
                    print('looking for J_Go')
                    if browser.find_element_by_id("J_Go"):
                        print('find J_Go')
                        browser.find_element_by_xpath('//*[@id="J_Go"]').click()
                        print("结算成功")
                except KeyboardInterrupt:
                    sys.exit(0)

                while True:
                    try:
                        print('looking for 提交订单按钮')
                        if browser.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]'):
                            print('find 提交订单按钮')
                            browser.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]').click()
                            now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            print("抢购成功时间：%s" % now1)
                            break
                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        print("再次尝试提交订单")
                    time.sleep(0.01)
            else:
                print('时间不到')
                time.sleep(3)

    def login(self, browser=None):

        # 打开淘宝登录页，并进行扫码登录
        print('start login')
        browser.get(
            "https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9PaEMvC&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
        browser.find_element_by_xpath("//*[@id='login']/div[1]/i").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")
        time.sleep(3)
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    times = input("请输入抢购时间，格式如(2018-09-06 11:26:00.000000):")
    # 时间格式："2019-01-24 12:17:00.000000"
    browser = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    print('start chrome done')
    browser.maximize_window()
    print('maximize chrome done,gonna login')
    MiaoSha().login(browser)
    # choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    choose = 1
    MiaoSha().buy(times, choose, browser)
