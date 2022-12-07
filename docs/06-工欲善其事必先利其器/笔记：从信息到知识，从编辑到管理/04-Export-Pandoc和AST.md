# AST

AST，Abstract Syntax对于JavaScript而言，AST是一个很重要的概念。



# Pandoc

> 本文侧重点主要在Markdown到HTML的过程，对其他格式可能会暂时提及较少。

文件格式转换神器，越用越香（刚开始的不香都是因为在用我自己愚蠢、保守的思想去揣度pandoc的可扩展性）。

提前预告完全体命令（个人目前用的）

```bash
pandoc in.md -o out.html --template=github --css=http://47.103.199.15/css/paper.css --mathjax=http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default
```



## 基础使用

```bash
pandoc in.md -o out.html
```

**但这样生成的只是html fragment，即单纯的将markdown格式转换为了html文档格式，没有新增任何文档元信息（如head标签等内容）**

可以通过`-c`添加CSS（可以理解为一种文档元数据）。

```bash
pandoc in.md -c style.css -o out.html
```

## Pandoc工作机制

### Markdown解析器

> 引自typora文档
>
> If you run Pandoc from command line, then you need to specify its markdown parser (from Pandoc Markdown, [CommonMark](http://commonmark.org/), [PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/), [GitHub-Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)).

> Pandoc文档
>
> Pandoc has a modular design: it consists of a set of readers, which parse text in a given format and produce a native representation of the document (an *abstract syntax tree* or AST), and a set of writers, which convert this native representation into a target format.

pandoc是模块化的，通过markdown解析器将文档解析成抽象语法树。

用Typora导出文件的时候，虽然Typora也要经pandoc转换，但Typora将自己内部根据文档生成的AST传给pandoc，从而不需要用pandoc的markdown解析器。

所以用Typora导出的html/PDF跟在Typora编辑器内看到的markdown一样整洁——妙啊。

### Pnadoc Filters

> Pandoc provides an interface for users to write programs (known as filters) which act on pandoc’s AST.
>
> INPUT --reader--> AST --filter--> AST --writer--> OUTPUT

Pandoc supports two kinds of filter: Lua filters and JSON filter.

关于Filters的内容很多……但我不太想深入，就先搁置了。





## Template

使用参数`-s/--standalone`可以导出完整文档，而pandoc是根据模板导出完整文档的。pandoc会有一个默认的模板，参数`--template`可以指定自定义的模板。



命令`pandoc -D format`可以查看特定format的默认模板。如`pandoc -D html`会有如下信息：

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="$lang$" xml:lang="$lang$"$if(dir)$ dir="$dir$"$endif$>
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
$for(author-meta)$
  <meta name="author" content="$author-meta$" />
$endfor$
$if(date-meta)$
  <meta name="dcterms.date" content="$date-meta$" />
$endif$
$if(keywords)$
  <meta name="keywords" content="$for(keywords)$$keywords$$sep$, $endfor$" />
$endif$
  <title>$if(title-prefix)$$title-prefix$ – $endif$$pagetitle$</title>
  <style type="text/css">
      code{white-space: pre-wrap;}
      span.smallcaps{font-variant: small-caps;}
      span.underline{text-decoration: underline;}
      div.column{display: inline-block; vertical-align: top; width: 50%;}
$if(quotes)$
      q { quotes: "“" "”" "‘" "’"; }
$endif$
  </style>
$if(highlighting-css)$
  <style type="text/css">
$highlighting-css$
  </style>
$endif$
$for(css)$
  <link rel="stylesheet" href="$css$">
$endfor$
$if(math)$
  $math$
$endif$
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
$for(header-includes)$
  $header-includes$
$endfor$
</head>
<body>
$for(include-before)$
$include-before$
$endfor$
$if(title)$
<header>
<h1 class="title">$title$</h1>
$if(subtitle)$
<p class="subtitle">$subtitle$</p>
$endif$
$for(author)$
<p class="author">$author$</p>
$endfor$
$if(date)$
<p class="date">$date$</p>
$endif$
</header>
$endif$
$if(toc)$
<nav id="$idprefix$TOC">
$table-of-contents$
</nav>
$endif$
$body$
$for(include-after)$
$include-after$
$endfor$
</body>
</html>
```



### data-dir

即pandoc的数据目录，直接引用一下官方原话

> Specify the user data directory to search for pandoc data files. If this option is not specified, the default user data directory will be used. On *nix and macOS systems this will be the `pandoc` subdirectory of the XDG data directory (by default, `$HOME/.local/share`, overridable by setting the `XDG_DATA_HOME` environment variable). If that directory does not exist, `$HOME/.pandoc` will be used (for backwards compatibility). In Windows the default user data directory is `C:\Users\USERNAME\AppData\Roaming\pandoc`. You can find the default user data directory on your system by looking at the output of `pandoc --version`. A `reference.odt`, `reference.docx`, `epub.css`, `templates`, `slidy`, `slideous`, or `s5` directory placed in this directory will override pandoc’s normal defaults.

当指定参数时，Pandoc会在该目录下搜索内容。以template为例：

![image-20201207154849382](C:\Users\Five\Desktop\note\img\image-20201207154849382.png)



### 语法

* `$--  comments --$`





## 数学公式渲染

**指定数学公式渲染引擎**，很重要，加粗

```bash
pandoc in.md --mathjax -o out.html
```

但这还不够，pandoc默认地mathjax引擎不一定能用，最好自己指定一个能用mathjaxJS引擎，如：

```bash
pandoc in.md --mathjax=http://cdn.mathjax.org/mathjax/latest/MathJax.jsconfig=default -o out.html
```

> 还是一样经过了摸爬滚打，才知道pandoc是`这样`用的，刚开始还傻乎乎地去html里加代码：
>
> `<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>`

经过以上，数学表达式就能正常显示了，效果如下图所示：

![image-20201017202048327](C:/Users/Five/Desktop/note/img/image-20201017202048327.png)

虽然mathjax只是LaTeX数学符号的一个子集，但一般很够用了。



## 转LaTeX/PDF

指定TeX引擎

```bash
pandoc in.md -o out.pdf --latex-engine=xelatex
```

> [Eisvogel](https://link.zhihu.com/?target=https%3A//github.com/Wandmalfarbe/pandoc-latex-template)，A clean pandoc LaTeX template to convert your markdown files to PDF or LaTeX。

https://github.com/Wandmalfarbe/pandoc-latex-template

先搁置，还没到用markdown写论文的地步（也许毕设会用）。

### 兼容中文

latex的中文素来麻烦。









# LLVM Style

学C++无意间注意到LLVM官网的CSS代码是真滴少（两个CSS文件加起来几十行），跟我的思路几乎一致。





[^1]: [pandoc官方文档](https://pandoc.org/MANUAL.html)
[^2]:[AST for JavaScript developers](https://itnext.io/ast-for-javascript-developers-3e79aeb08343)
[^3]:[Python AST官方文档](https://docs.python.org/zh-cn/3.7/library/ast.html)