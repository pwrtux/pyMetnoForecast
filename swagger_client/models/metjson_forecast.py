# coding: utf-8

"""
    Locationforecast

    Weather forecast for a specified place  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: weatherapi-adm@met.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class METJSONForecast(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'geometry': 'PointGeometry',
        'properties': 'Forecast',
        'type': 'str'
    }

    attribute_map = {
        'geometry': 'geometry',
        'properties': 'properties',
        'type': 'type'
    }

    def __init__(self, geometry=None, properties=None, type=None):  # noqa: E501
        """METJSONForecast - a model defined in Swagger"""  # noqa: E501
        self._geometry = None
        self._properties = None
        self._type = None
        self.discriminator = None
        self.geometry = geometry
        self.properties = properties
        self.type = type

    @property
    def geometry(self):
        """Gets the geometry of this METJSONForecast.  # noqa: E501


        :return: The geometry of this METJSONForecast.  # noqa: E501
        :rtype: PointGeometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this METJSONForecast.


        :param geometry: The geometry of this METJSONForecast.  # noqa: E501
        :type: PointGeometry
        """
        if geometry is None:
            raise ValueError("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

    @property
    def properties(self):
        """Gets the properties of this METJSONForecast.  # noqa: E501


        :return: The properties of this METJSONForecast.  # noqa: E501
        :rtype: Forecast
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this METJSONForecast.


        :param properties: The properties of this METJSONForecast.  # noqa: E501
        :type: Forecast
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this METJSONForecast.  # noqa: E501


        :return: The type of this METJSONForecast.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this METJSONForecast.


        :param type: The type of this METJSONForecast.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Feature"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(METJSONForecast, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, METJSONForecast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other