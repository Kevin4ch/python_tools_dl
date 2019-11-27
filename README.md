# python_tools_dl
### TransformsPadding
Pytorch Transforms for Padding

#### How to use
```
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(0.2, 0.2, 0.2),
    transforms.RandomRotation(5),
    Padding((32, 320)),
    transforms.ToTensor()])
```
#### Example
![Image text](https://github.com/Kevin4ch/python_tools_dl/blob/master/example_padding.png)
