# coding: utf-8

"""
    style-api

    This is a API document for Stylens Service

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetObjectsResponseData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'boxes': 'BoxesArray',
        'image_id': 'str'
    }

    attribute_map = {
        'boxes': 'boxes',
        'image_id': 'image_id'
    }

    def __init__(self, boxes=None, image_id=None):
        """
        GetObjectsResponseData - a model defined in Swagger
        """

        self._boxes = None
        self._image_id = None

        if boxes is not None:
          self.boxes = boxes
        if image_id is not None:
          self.image_id = image_id

    @property
    def boxes(self):
        """
        Gets the boxes of this GetObjectsResponseData.

        :return: The boxes of this GetObjectsResponseData.
        :rtype: BoxesArray
        """
        return self._boxes

    @boxes.setter
    def boxes(self, boxes):
        """
        Sets the boxes of this GetObjectsResponseData.

        :param boxes: The boxes of this GetObjectsResponseData.
        :type: BoxesArray
        """

        self._boxes = boxes

    @property
    def image_id(self):
        """
        Gets the image_id of this GetObjectsResponseData.

        :return: The image_id of this GetObjectsResponseData.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this GetObjectsResponseData.

        :param image_id: The image_id of this GetObjectsResponseData.
        :type: str
        """

        self._image_id = image_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetObjectsResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
