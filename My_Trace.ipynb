import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie
import numpy as np
"""
Gallery 使用 pyecharts 1.0.0
参考地址: https://gallery.echartsjs.com/editor.html?c=xSkGI6zLmb
目前无法实现的功能:
1、
"""
color_value = np.random.uniform(0, 100, [50])
data = [
    {
        "time": 2012,
        "data": [
            {"name": "贵州", "value": [color_value[0], 0,"贵阳 空军飞行员体检—初检"]},
            {"name": "四川", "value": [color_value[1],0,"成都 空军飞行员体检—复检，被淘汰了，dream stop here"]},
        ],
    },
    {
        "time": 2013,
        "data": [
            {"name": "福建", "value": [color_value[0], 0, "厦门 记忆总是美好，有机会再去一次"]},
            {"name": "辽宁", "value": [color_value[1], 0, "沈阳 我在东北大学生活了四年"]},
        ],
    },
    {
        "time": 2015,
        "data": [
            {"name": "河北", "value": [color_value[0], 0, "秦皇岛 与yuan的海滨度假"]},
            {"name": "北京", "value": [color_value[1], 0, "北京"]},
        ],
    },
    {
        "time": 2016,
        "data": [
            {"name": "吉林", "value": [color_value[0], 0, "长春 看望李建安，我的飞行员哥们"]},
            {"name": "北京", "value": [color_value[1], 0, "北京"]},
        ],
    },
    {
        "time": 2018,
        "data": [
            {"name": "北京", "value": [color_value[0], 0, "北京 开始了研究生生活"]},
            {"name": "陕西", "value": [color_value[1], 0, "西安 在古城墙上骑自行车"]},
            {"name": "江苏", "value": [color_value[2], 0, "南京 计算力学大会"]},
        ],
    },
    {
        "time": 2019,
        "data": [
            {"name": "北京", "value": [color_value[0], 0, "北京","None"]},
            {"name": "安徽", "value": [color_value[1], 0, "黄山","下山的时候腿都在抖"]},
            {"name": "黑龙江", "value": [color_value[2], 0, "哈尔滨","固体力学大会"]},
        ],
    },
    {
        "time": 9999,
        "data": [
            {"name": "贵州", "value": [color_value[0], 0,"贵阳","空军飞行员体检—初检"]},
            {"name": "四川", "value": [color_value[1],0,"成都","空军飞行员体检—复检，被淘汰了，dream stop here"]},
            {"name": "福建", "value": [color_value[2], 0, "厦门","记忆总是美好，有机会再去一次"]},
            {"name": "辽宁", "value": [color_value[3], 0, "沈阳","我在东北大学生活了四年"]},
            {"name": "河北", "value": [color_value[4], 0, "秦皇岛","与yuan的海滨度假"]},
            {"name": "吉林", "value": [color_value[5], 0, "长春","看望李建安，我的飞行员哥们"]},
            {"name": "北京", "value": [color_value[6], 0, "北京","开始了研究生生活"]},
            {"name": "陕西", "value": [color_value[7], 0, "西安","在古城墙上骑自行车"]},
            {"name": "江苏", "value": [color_value[8], 0, "南京","计算力学大会"]},
            {"name": "安徽", "value": [color_value[9], 0, "黄山","下山的时候腿都在抖"]},
            {"name": "黑龙江", "value": [color_value[10], 0, "哈尔滨","固体力学大会"]},
        ],
    },
]


def get_year_chart(year: int):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == year
    ][0]
    min_data, max_data = (
        min([d[1][0] for d in map_data]),
        max([d[1][0] for d in map_data]),
    )
    map_chart = (
        Map()
        .add(
            series_name="",
            data_pair=map_data,
            label_opts=opts.LabelOpts(is_show=False),
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="记录我到过的地方",
                subtitle="读万卷书，行万里路（不同颜色仅为了区别省份，无其他意义）",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(0,0,0, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[3];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=False,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#333"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )
    return map_chart


# Draw Timeline
time_list = [9999, 2012, 2013, 2015 ,2016, 2018, 2019]
# time_list = [9999]
timeline = Timeline(
    init_opts=opts.InitOpts(width="auto", height="500px", theme=ThemeType.WALDEN)
)
for y in time_list:
    g = get_year_chart(year=y)
    timeline.add(g, time_point=str(y))

timeline.add_schema(
    orient="vertical",
    is_auto_play=False,
    is_inverse=False,
    play_interval=5000,
    pos_left="null",
    pos_right="5",
    pos_top="20",
    pos_bottom="20",
    width="50",
    label_opts=opts.LabelOpts(is_show=True, color="#000"),
)

timeline.render("My_Trace_Map.html")
