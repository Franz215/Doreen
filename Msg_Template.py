from linebot.models import *
def stock_reply_rate():
    content_text = "想知道匯率?"
    text_message = TextSendMessage(
                               text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜查詢單一幣別匯率", 
                                                    text="幣別種類",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜查詢幣別匯率",
                                                    text="匯率兌換",
                                                )
                                           
                                       ),
                                       QuickReplyButton(
                                           action=MessageAction(
                                               label="💜💜查詢幣別匯率",
                                               text="我的外幣",                                               
                                           )
                                       ),
                                   ]

                                ))
    return text_message

def stock_reply_other():
    content_text = "分析趨勢圖"
    text_message = TextSendMessage(
                                text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                           action=MessageAction(
                                               label="❤️即時股價❤️",
                                               text="股價查詢->#2330",
                                           )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="❤️匯率圖❤️",
                                                    text="@k股票代號日期區間->@k23302024-01-01",
                                                    )
                                           ),
                                   ]
                               ))
    return text_message
# 測試的button
def test_Button():
    flex_message = FlexSendMessage(
            alt_text="Test",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/RQUdSTk.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://line.me/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "美金",
                        "text": "USD"
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "台幣",
                        "text": "TWD"
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "南非幣",
                        "text": "ZAR"
                        }
                    }
                    ]
                }
                }
    )
    return flex_message
    
# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/RQUdSTk.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://line.me/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "美金",
                            "text": "USD"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "日元",
                            "text": "JPY"
                            }
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "南非幣",
                            "text": "ZAR"
                            }
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "歐元",
                                "text": "EUR"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "英鎊",
                                "text": "GBP"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "加幣",
                                "text": "CAD"
                                }
                            }
                            ]
                        }
                        ],
                        "spacing": "sm"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "澳幣",
                                "text": "AUD"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "紐幣",
                                "text": "NZD"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "瑞郎",
                                "text": "CHF"
                                }
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": []
                    }
                    ],
                    "spacing": "sm",
                    "backgroundColor": "#484891",
                    "borderColor": "#FFBB77",
                    "borderWidth": "normal",
                    "margin": "sm"
                }
        }               
    )
    return flex_message

# 理財頻道
def youtube_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/SJPH542.jpg",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "size": "full",
                        "backgroundColor": "#000000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財達人秀",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "最精彩最好懂",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/channel/UCQvsuaih5lE0n_Ne54nNezg"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/dPW0jcC.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#AA0000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CMoney理財寶",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "基本理財知識",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/CMoneySchool"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/zkUZrCj.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#444444"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "我要做富翁",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "平民化&分享形式",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/SyLingHim"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message
def realtime_currency_other(currency):
    content = "想知道更多?"
    text_message = TextSendMessage(
                                text = content ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="即時匯率", 
                                                    text="外幣"+currency,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="加入清單", 
                                                    text="新增外幣"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text="N外匯"+currency,
                                                )
                                       )
                                ]
                            ))
    return text_message
