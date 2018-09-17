#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: dyn date: 2018/9/17

# 向本地gym库添加编写好的新环境后test

import gym

id = "SkullAndTreasure-v0"	 # 设置环境id
env = gym.make(id)	# 构建环境对象
env.reset()	# 重置环境
env.render()	# 绘制环境
input("press any key to continue...")
env.close()	# 关闭环境
