import React, { Component } from 'react';
import Table from 'react-bootstrap/Table';
import dateConverter from '../../utils/utils';

class Comment extends Component {
	render() {
		return (
			<Table striped>
				<tbody>
					<tr>
						<td>
							<p><b>{this.props.item.author}</b> - <i>{dateConverter(this.props.item.published_time)}</i></p>
						</td>
					</tr>
					<tr>
						<td>
							<p>{this.props.item.content}</p>
						</td>
					</tr>
				</tbody>
			</Table>
		);
	}
}


export default Comment;
