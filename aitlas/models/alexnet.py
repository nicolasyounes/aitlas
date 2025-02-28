import torch.nn as nn
import torchvision.models as models

from ..base import BaseMulticlassClassifier, BaseMultilabelClassifier


class AlexNet(BaseMulticlassClassifier):
    name = "AlexNet"

    def __init__(self, config):
        super().__init__(config)

        if self.config.pretrained:
            self.model = models.alexnet(self.config.pretrained, False)
            self.model.classifier = self.model.classifier[:-1]  # remove final layer
            self.model.classifier.add_module(
                "6", nn.Linear(4096, self.config.num_classes, bias=True)
            )
            if self.config.freeze:
                self.freeze()
        else:
            self.model = models.alexnet(
                self.config.pretrained, False, num_classes=self.config.num_classes
            )

    def forward(self, x):
        return self.model(x)

    def extract_features(self):
        """ Remove final layers if we only need to extract features """
        self.model.classifier = self.model.classifier[:-3]

        return self.model

    def freeze(self):
        for param in self.model.parameters():
            param.require_grad = False
        for param in self.model.classifier.parameters():
            param.require_grad = True


class AlexNetMultiLabel(BaseMultilabelClassifier):
    name = "AlexNet"

    def __init__(self, config):
        super().__init__(config)

        if self.config.pretrained:
            self.model = models.alexnet(self.config.pretrained, False)
            self.model.classifier = self.model.classifier[:-1]  # remove final layer
            self.model.classifier.add_module(
                "6", nn.Linear(4096, self.config.num_classes, bias=True)
            )
            if self.config.freeze:
                self.freeze()

        else:
            self.model = models.alexnet(
                self.config.pretrained, False, num_classes=self.config.num_classes
            )

    def forward(self, x):
        return self.model(x)

    def extract_features(self):
        """ Remove final layers if we only need to extract features """
        self.model.classifier = self.model.classifier[:-3]

        return self.model

    def freeze(self):
        for param in self.model.parameters():
            param.require_grad = False
        for param in self.model.classifier.parameters():
            param.require_grad = True
