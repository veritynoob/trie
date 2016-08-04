#!/usr/bin/env python
#coding=utf-8
'''
    Created on 2011-07-12
    @author: devingong
    @desc:
        python 前缀树
    @usage:
        前缀树的使用分为构建TrieTree和查找两个过程
        构建方法：
            trie = TrieTree()
            trie.insert(str)
            ...
            trie.insert(str)
        提供两种方法进行查找：
            trie.find(str)  该方法一旦发现有匹配的串，立即返回
            trie.findMax(str)   该方法会返回最长的匹配串
        注意：中文的时候，构建和查找的时候编码需要一致
'''
import sys

class Node:
    '''
        前缀树的节点
    '''
    def __init__(self):
        self.value = None       #节点的值
        self.childs = {}        #用set保存孩子节点
        self.isData = False     #是否为数据节点
        
    def hasChild(self, v):
        '''
            判断是否有value为v的孩子节点
        '''
        if v in self.childs:
            return True
        else:
            return False
    
    def addChild(self, v):
        '''
            添加孩子
        '''
        child = Node()
        child.value = v
        self.childs[v] = child
        
        return child

    def getChild(self, v):
        '''
            获得value为v的孩子节点
        '''
        if v in self.childs:
            return self.childs[v]
        else:
            return None

class TrieTree:
    '''
        前缀树
    '''
    def __init__(self):
        self.root = Node()      #根节点
        self.size = 0           #记录不同的节点个数
        self.maxHeight = 0      #记录树高
        self.minHeight = sys.maxint     #记录树最小层次

    def insert(self, data):
        '''
            添加数据构建TrieTree
        '''
        node = self.root
        if len(data) > self.maxHeight:
            self.maxHeight = len(data)
        if len(data) < self.minHeight:
            self.minHeight = len(data)
        
        for v  in data[:-1]:
            child = node.getChild(v)
            if child == None:
                child = node.addChild(v)
            node = child
        
        v = data[-1]
        child = node.getChild(v)
        if child == None:
            child = node.addChild(v)

        if not child.isData:
            self.size += 1
            child.isData = True
        
    def find(self, data):
        '''
            查找是否有匹配串
            返回匹配的长度，没有匹配返回0
        '''
        node = self.root
        
        num = 0
        for v in data:
            child = node.getChild(v)
            if child == None:
                return 0
            else:
                node = child
                num += 1
            
            if node.isData:
                return num
            
        return 0
        
    def findMax(self, data):
        '''
            查找最大的匹配串
            返回匹配的长度，没有匹配返回0
        '''
        node = self.root
               
        num = 0
        maxNum = 0
        for v in data:
            child = node.getChild(v)
            if child == None:
               break
            else:
               node = child
               num += 1
            if node.isData:
                if num > maxNum:
                    maxNum = num
            
        return maxNum
    


if __name__ == '__main__':
    trieTree = TrieTree()

    trieTree.insert('a')
    trieTree.insert('b')
    trieTree.insert('s')
    trieTree.insert('人民')
    
    print trieTree.find('s')
    _str = '人名'
    print trieTree.findMax(_str), len(_str)
