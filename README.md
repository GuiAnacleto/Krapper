![Krapper](https://user-images.githubusercontent.com/30503293/109403244-bebc2f00-793a-11eb-821b-63040cbea9f8.png)

![Build Status](https://img.shields.io/github/downloads/GuiAnacleto/Krapper/total) ![Build Status](https://img.shields.io/github/v/release/GuiAnacleto/Krapper)

# Krapper

Krapper is a program that can enter in TikTok application and Scrapp User/Video Data in a csv. Common used to marketin analytics.

# Features

- Input any `Hashtag` and watch the magic
- Select `Trending` option and take all trending videos in one shot
- Choose the `Amount` results you need to see.
- Stupidly [`easy to use`](https://github.com/GuiAnacleto/Krapper#usage)
- Easy installation necessary - just use the [`step by step`](https://github.com/GuiAnacleto/Krapper#installation).

# Installation

Krapper requires [`python`](https://www.pytho.org/downloads/) V3.8+ to run.
Install the python librarys:

![carbon](https://user-images.githubusercontent.com/30503293/109400754-3e410280-7929-11eb-8ce4-0a48fccfb00c.png)

`Execute` this commands in windows prompt `CMD` after installerd python:

```bash
$ pip install pandas
$ pip install pysimplegui
$ pip install tiktokapi
$ pip install numpy
```

Also you have to install playwright, go to the folther that you downloaded Krapper.
Go to your folder in Windows Prompt:

```bash
$ cd "your path"/Krapper
```

And run the above code:

```bash
$ cd python -m playwright install
```

After This you Can Run the Krapper!! 👍

## Another Installation Option

If do not want lead with python librarys, you can install just one library in your main computer:

```bash
$ pip install virtualenv
```

After install this library you have to clone this repository.

```bash
$ git clone https://github.com/GuiAnacleto/Krapper
```

So, go to your project folder and run:

```bash
$ virtualenv env
```

This will generate an folder named `env`, this folder simule your main machine. After the instalation `start` de virtual ambient executing the command above:

```bash
$ cd env\Scripts
$ .\activate
```

One time that the virtual ambient is activate, you have just to install all librarys that have been passed in step one...
One time that the virtual ambient is activated, you can run python file in your TextEditor.

To do this, execute:

```bash
$ cd..
$ cd..
$ python main.py
```

After This you Can Run the Krapper!! 👍

# Usage

### Buttons:
| Buttom | Function |
| ------ | ------ |
| SearchTerm | In this label you insert the hashtag. |
| Hashtag | When this radio button is true the program will consider the serach term. |
| Trending | This radio button do not consider the searchterm for results. |
| Browse | Enable file dialog to select folder destiny. |
| Search | Start the TikTok Scrapping |
| +10 / -10 | Plus 10 or Sub 10 of the quantity |

### Functionalities:

To use the Krapper you just to select if you want an hashtag or trending search in radio buttons. If you select `HASHTAG`, then input the term that you want to be your hashtag, after this, click in `BROWSE` and select the `DESTINATION` folder. Input the name of the archive in correct label. So finally click in `SEARCH`. Wait for the `FINISH` pop up. 

![Capturar](https://user-images.githubusercontent.com/30503293/109402741-24a6b780-7937-11eb-8d4a-32af48f325ab.PNG)



And here you have your result!! Enjoy 👍

## Contributing

#### Bug Reports & Feature Requests

Please use the [`issue tracker`](https://github.com/GuiAnacleto/Krapper/issues) to report any bugs or file feature requests.

#### Developing

PRs are welcome. To begin developing, do this:

```bash
$ git clone git@github.com:GuiAnacleto/Krapper.git
$ cd Code/
$ python main.py
```
