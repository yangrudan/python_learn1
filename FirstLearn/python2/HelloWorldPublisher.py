# Copyright 2022 Proyectos y Sistemas de Mantenimiento SL (eProsima).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
HelloWorld Publisher
"""
from threading import Condition
import time

import fastdds
import HelloWorld



DESCRIPTION = """HelloWorld Publisher example for Fast DDS python bindings"""
USAGE = ('python3 HelloWorldPublisher.py')

class WriterListener (fastdds.DataWriterListener) :
    def __init__(self, writer) :
        self._writer = writer
        super().__init__()


    def on_publication_matched(self, datawriter, info) :
        if (0 < info.current_count_change) :
            print ("Publisher matched subscriber {}".format(info.last_subscription_handle))
            self._writer._cvDiscovery.acquire()
            self._writer._matched_reader += 1
            self._writer._cvDiscovery.notify()
            self._writer._cvDiscovery.release()
        else :
            print ("Publisher unmatched subscriber {}".format(info.last_subscription_handle))
            self._writer._cvDiscovery.acquire()
            self._writer._matched_reader -= 1
            self._writer._cvDiscovery.notify()
            self._writer._cvDiscovery.release()


class Writer:


    def __init__(self):
        self._matched_reader = 0
        self._cvDiscovery = Condition()
        self.index = 0

        factory = fastdds.DomainParticipantFactory.get_instance()
        '''
        self.participant_qos = fastdds.DomainParticipantQos()
        factory.get_default_participant_qos(self.participant_qos)
        shm = fastdds.TransportDescriptorInterfaceShrPtr()
        vec_shm2 = fastdds.TransportDescriptorInterfaceVector()
        vec_shm2.clear()
        vec_shm2.append(shm)
        cfg_qos = fastdds.TransportConfigQos()

        print("ddd",type(cfg_qos.user_transports))
        self.participant_qos.transport(cfg_qos)
        '''
        factory.load_XML_profiles_file('my_profile2.xml')
        #self.participant = factory.create_participant(0, self.participant_qos)
        self.participant = factory.create_participant_with_profile('SHMParticipant')
        print('participant [reg type] is {}'.format(self.participant.register_type))

        '''
        print(fastdds.TransportConfigQos.send_socket_buffer_size)
        print(fastdds.TransportConfigQos.listen_socket_buffer_size)
        print(not fastdds.TransportConfigQos.use_builtin_transports)
        print("\n111", fastdds.TransportConfigQos.user_transports.getter)
        print("\nsss", self.participant_qos)
        print("\n222", self.participant_qos.name())
        print(self.participant_qos.user_data())
        print("==========================================")
        print(self.participant.register_type)
        '''

        self.topic_data_type = HelloWorld.HelloWorldPubSubType()
        self.topic_data_type.setName("HelloWorld")
        self.type_support = fastdds.TypeSupport(self.topic_data_type)
        self.participant.register_type(self.type_support)

        self.topic_qos = fastdds.TopicQos()
        self.participant.get_default_topic_qos(self.topic_qos)
        self.topic = self.participant.create_topic("HelloWorldTopic", self.topic_data_type.getName(), self.topic_qos)

        self.publisher_qos = fastdds.PublisherQos()
        self.participant.get_default_publisher_qos(self.publisher_qos)
        self.publisher = self.participant.create_publisher(self.publisher_qos)

        self.listener = WriterListener(self)
        self.writer_qos = fastdds.DataWriterQos()
        self.publisher.get_default_datawriter_qos(self.writer_qos)
        self.writer = self.publisher.create_datawriter(self.topic, self.writer_qos, self.listener)


    def write(self):
        data = HelloWorld.HelloWorld()
        data.message("Hello World------------------")
        data.index(self.index)
        self.writer.write(data)
        print(writer.type_support.get_type_name())#yang debug
        print("Sending {message} : {index}".format(message=data.message(), index=data.index()))
        self.index = self.index + 1


    def wait_discovery(self) :
        self._cvDiscovery.acquire()
        print ("Writer is waiting discovery...")
        self._cvDiscovery.wait_for(lambda : self._matched_reader != 0)
        self._cvDiscovery.release()
        print("Writer discovery finished...")


    def run(self):
        self.wait_discovery()
        for x in range(10) :
            time.sleep(1)
            self.write()
        self.delete()


    def delete(self):
        factory = fastdds.DomainParticipantFactory.get_instance()
        self.participant.delete_contained_entities()
        factory.delete_participant(self.participant)


if __name__ == '__main__':
    print('Starting publisher.')
    writer = Writer()
    writer.run()
    exit()