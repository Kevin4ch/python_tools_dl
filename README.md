# python_tools_dl
##### TransformsPadding
Pytorch Transforms for Padding
```
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(0.2, 0.2, 0.2),
    transforms.RandomRotation(5),
    Padding((32, 320)),
    transforms.ToTensor()])
```
![Image text](https://raw.githubusercontent.com/hongmaju/light7Local/master/img/productShow/20170518152848.png)
