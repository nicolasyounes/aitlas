import torch.nn as nn
import torchvision.models as models

from ..base import BaseMulticlassClassifier, BaseMultilabelClassifier


class DenseNet161(BaseMulticlassClassifier):
    name = "DenseNet161"

    def __init__(self, config):
        super().__init__(config)

        if self.config.pretrained:
            self.model = models.densenet161(self.config.pretrained, False)
            num_ftrs = self.model.classifier.in_features
            self.model.classifier = nn.Linear(num_ftrs, self.config.num_classes)
            if self.config.freeze:
                self.freeze()
        else:
            self.model = models.densenet161(
                self.config.pretrained, False, num_classes=self.config.num_classes
            )

    def forward(self, x):
        return self.model(x)

    def extract_features(self):
        """ Remove final layers if we only need to extract features """
        self.model = nn.Sequential(*list(self.model.children())[:-1])

        return self.model

    def freeze(self):
        for param in self.model.parameters():
            param.require_grad = False
        for param in self.model.classifier.parameters():
            param.require_grad = True


class DenseNet161MultiLabel(BaseMultilabelClassifier):
    name = "DenseNet161"

    def __init__(self, config):
        super().__init__(config)

        if self.config.pretrained:
            self.model = models.densenet161(self.config.pretrained, False)
            num_ftrs = self.model.classifier.in_features
            self.model.classifier = nn.Linear(num_ftrs, self.config.num_classes)
            if self.config.freeze:
                self.freeze()
        else:
            self.model = models.densenet161(
                self.config.pretrained, False, num_classes=self.config.num_classes
            )

    def forward(self, x):
        return self.model(x)

    def extract_features(self):
        """ Remove final layers if we only need to extract features """
        self.model = nn.Sequential(*list(self.model.children())[:-1])

        return self.model

    def freeze(self):
        for param in self.model.parameters():
            param.require_grad = False
        for param in self.model.classifier.parameters():
            param.require_grad = True
