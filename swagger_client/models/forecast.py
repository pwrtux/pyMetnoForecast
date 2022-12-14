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

class Forecast(object):
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
        'meta': 'ForecastMeta',
        'timeseries': 'list[ForecastTimeStep]'
    }

    attribute_map = {
        'meta': 'meta',
        'timeseries': 'timeseries'
    }

    def __init__(self, meta=None, timeseries=None):  # noqa: E501
        """Forecast - a model defined in Swagger"""  # noqa: E501
        self._meta = None
        self._timeseries = None
        self.discriminator = None
        self.meta = meta
        self.timeseries = timeseries

    @property
    def meta(self):
        """Gets the meta of this Forecast.  # noqa: E501


        :return: The meta of this Forecast.  # noqa: E501
        :rtype: ForecastMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Forecast.


        :param meta: The meta of this Forecast.  # noqa: E501
        :type: ForecastMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def timeseries(self):
        """Gets the timeseries of this Forecast.  # noqa: E501


        :return: The timeseries of this Forecast.  # noqa: E501
        :rtype: list[ForecastTimeStep]
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """Sets the timeseries of this Forecast.


        :param timeseries: The timeseries of this Forecast.  # noqa: E501
        :type: list[ForecastTimeStep]
        """
        if timeseries is None:
            raise ValueError("Invalid value for `timeseries`, must not be `None`")  # noqa: E501

        self._timeseries = timeseries

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
        if issubclass(Forecast, dict):
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
        if not isinstance(other, Forecast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
