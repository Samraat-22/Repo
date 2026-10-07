import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

input_size = 28 * 28  # 784
num_classes = 10
num_epochs = 5
batch_size = 100
learning_rate = 0.001

train_dataset = torchvision.datasets.MNIST(
    root='../../data', train=True, transform=transforms.ToTensor(), download=True
)

test_dataset = torchvision.datasets.MNIST(
    root='../../data', train=False, transform=transforms.ToTensor()
)


train_loader = torch.utils.data.DataLoader(
    dataset=train_dataset, batch_size=batch_size, shuffle=True
)

test_loader = torch.utils.data.DataLoader(
    dataset=test_dataset, batch_size=batch_size, shuffle=False
)

model = nn.Linear(input_size, num_classes)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)


epoch_losses = []
step_losses = []


total_step = len(train_loader)
for epoch in range(num_epochs):
  running_loss = 0.0
  for i, (images, labels) in enumerate(train_loader):
    # Reshape images to (batch_size, input_size)
    images = images.reshape(-1, input_size)

    # Forward pass
    outputs = model(images)
    loss = criterion(outputs, labels)

    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    running_loss += loss.item()
    if (i + 1) % 100 == 0:
      step_losses.append(loss.item())
      print(
          "Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}".format(
              epoch + 1, num_epochs, i + 1, total_step, loss.item()
          )
      )

  # Track average epoch loss
  epoch_losses.append(running_loss / total_step)


with torch.no_grad():
  correct = 0
  total = 0
  for images, labels in test_loader:
    images = images.reshape(-1, input_size)
    outputs = model(images)
    _, predicted = torch.max(outputs.data, 1)
    total += labels.size(0)
    correct += (predicted == labels).sum()

print(
    "Accuracy of the model on the 10000 test images: {} %".format(
        100 * correct / total
    )
)


torch.save(model.state_dict(), "model.ckpt")


plt.figure(figsize=(10, 4))

# Plot 1: Epoch Loss Curve
plt.subplot(1, 2, 1)
plt.plot(range(1, num_epochs + 1), epoch_losses, marker='o', color='b')
plt.title('Training Loss per Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)

# Plot 2: Step-wise Loss Curve
plt.subplot(1, 2, 2)
plt.plot(step_losses, color='r')
plt.title('Training Loss per 100 Steps')
plt.xlabel('Steps (x100)')
plt.ylabel('Loss')
plt.grid(True)

plt.tight_layout()
plt.show()